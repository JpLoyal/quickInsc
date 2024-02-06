from django import forms
from datetime import time

from .models import Event

from .forms_validators import validate_age, valida_cpf


class ParticipantForm(forms.Form):

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]


    name = forms.CharField(label='Nome', max_length=100)
    age = forms.IntegerField(label='Idade', required=False, validators=[validate_age])
    CPF = forms.CharField(label='CPF', validators=[valida_cpf])
    gender = forms.ChoiceField(label='Sexo', choices=SEXO_CHOICES)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone')
    events = forms.ModelChoiceField(queryset=Event.objects.all(), label='Evento')


class EventForm(forms.Form):

    HOUR_CHOICES = [
        (time(hour, minute).strftime('%H:%M'), time(hour, minute).strftime('%H:%M')) for hour in range(24) for minute in [0, 15, 30, 45]
    ]


    name = forms.CharField(label='Nome do Evento')
    attractions = forms.CharField(label='Atrações')
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
    min_age = forms.IntegerField(label='Idade Mínima Permitida')
    date = forms.DateField(label='Data do Evento', widget=forms.SelectDateWidget())
    time_starts = forms.TimeField(label='Hora de Início', widget=forms.Select(choices=HOUR_CHOICES))
    time_ends = forms.TimeField(label='Hora de Término', widget=forms.Select(choices=HOUR_CHOICES))
    address = forms.CharField(label='Endereço')
