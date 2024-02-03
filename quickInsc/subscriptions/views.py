from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ParticipantForm

# Create your views here.

def subscription(request):

    if request.method == 'POST':
        form = ParticipantForm(request.POST)

        if not form.is_valid():
            return render(request, 'subscriptions.html', {'form': form})
        
        # caso válido, criar um no banco de dados
        # redireciona para página de sucesso
        return HttpResponseRedirect('sucess/')

    form = ParticipantForm()
    return render(request, 'subscriptions.html', {'form': form})


def subscription_sucess(request):
    return render(request, 'subscription_sucess.html')