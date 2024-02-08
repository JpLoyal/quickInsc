from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .forms import ParticipantForm, EventForm
from .models import Event, Participant

# Create your views here.

class SubscriptionPerson(View):

    def post(self, *args, **kwargs):
        form = ParticipantForm(self.request.POST)

        if not form.is_valid():
            return render(self.request, 'subscriptions_person.html', {'form': form})
        
        # Cria registro no banco de dados
        participant = Participant.objects.create(
            name=form.cleaned_data['name'],
            age=form.cleaned_data['age'],
            CPF=form.cleaned_data['CPF'],
            gender=form.cleaned_data['gender'],
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone'],
        )

        participant.events.add(form.cleaned_data['events'])

        # redireciona para página de sucesso
        return redirect('person_sucess', participant.id)
    
    def get(self, *args, **kwargs):
        form = ParticipantForm()
        return render(self.request, 'subscriptions_person.html', {'form': form})
 
    

class SubscriptionEvent(View):
     
    def post(self, *args, **kwargs):
        form = EventForm(self.request.POST)

        if not form.is_valid():
            return render(self.request, 'subscriptions_event.html', {'form': form})

        # Cria registro no banco de dados
        evento = Event.objects.create(**form.cleaned_data)
        
        # redireciona para página de sucesso
        return redirect('event_sucess', evento.id)
    
    def get(self, *args, **kwargs):
        form = EventForm()
        return render(self.request, 'subscriptions_event.html', {'form': form})



def subscription_person_sucess(request, pk):
    participante = Participant.objects.get(id=pk)
    return render(request, 'subscriptions_person_sucess.html', {'participante': participante})



def subscription_event_sucess(request, pk):
    evento = Event.objects.get(pk=pk)
    return render(request, 'subscriptions_event_sucess.html', {'evento': evento})

