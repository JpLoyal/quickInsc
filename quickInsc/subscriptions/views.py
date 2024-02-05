from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .forms import ParticipantForm, EventForm

# Create your views here.


class SubscriptionPerson(View):

    def post(self, *args, **kwargs):
        form = ParticipantForm(self.request.POST)

        if not form.is_valid():
            return render(self.request, 'subscriptions_person.html', {'form': form})
        
        # caso válido, criar um no banco de dados
        # redireciona para página de sucesso
        return HttpResponseRedirect('sucess/')
    
    def get(self, *args, **kwargs):
        form = ParticipantForm()
        return render(self.request, 'subscriptions_person.html', {'form': form})
 
    
class SubscriptionEvent(View):
     
    def post(self, *args, **kwargs):
        form = EventForm(self.request.POST)

        if not form.is_valid():
            return render(self.request, 'subscriptions_event.html', {'form': form})
        
        # caso válido, criar um no banco de dados
        # redireciona para página de sucesso
        return HttpResponseRedirect('sucess/')
    
    def get(self, *args, **kwargs):
        form = EventForm()
        return render(self.request, 'subscriptions_event.html', {'form': form})


class SubscriptionSucess(TemplateView):
    template_name = 'subscription_sucess.html'

