from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
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

        print(participant)
        
        participant.events.add(form.cleaned_data['events'])

        # redireciona para página de sucesso
        return HttpResponseRedirect('/subscriptions/sucess/')
    
    def get(self, *args, **kwargs):
        form = ParticipantForm()
        return render(self.request, 'subscriptions_person.html', {'form': form})
 
    
class SubscriptionEvent(View):
     
    def post(self, *args, **kwargs):
        form = EventForm(self.request.POST)

        if not form.is_valid():
            return render(self.request, 'subscriptions_event.html', {'form': form})

        # Cria registro no banco de dados
        Event.objects.create(**form.cleaned_data)
        
        # redireciona para página de sucesso
        return HttpResponseRedirect('/subscriptions/sucess/')
    
    def get(self, *args, **kwargs):
        form = EventForm()
        return render(self.request, 'subscriptions_event.html', {'form': form})


class SubscriptionSucess(TemplateView):
    template_name = 'subscription_sucess.html'

