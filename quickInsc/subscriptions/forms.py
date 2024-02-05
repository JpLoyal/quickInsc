from django import forms
from django.core.exceptions import ValidationError
from datetime import time


class ParticipantForm(forms.Form):

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]


    ### Validadores 
    
    def validate_age(value):
        if not value >= 18:
            raise ValidationError("A idade deve ser maior que 18 anos.")


    name = forms.CharField(label='Nome', max_length=100)
    age = forms.IntegerField(label='Idade', required=False, validators=[validate_age])
    CPF = forms.CharField(label='CPF')
    gender = forms.ChoiceField(label='Sexo', choices=SEXO_CHOICES)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone')


class EventForm(forms.Form):

    HOUR_CHOICES = [
        (time(hour, minute).strftime('%H:%M'), time(hour, minute).strftime('%H:%M')) for hour in range(24) for minute in [0, 15, 30, 45]
    ]


    name = forms.CharField(label='Nome do Evento')
    attractions = forms.CharField(label='Atrações')
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
    date = forms.DateField(label='Data')
    time_starts = forms.TimeField(label='Hora de Início', widget=forms.Select(choices=HOUR_CHOICES))
    time_ends = forms.TimeField(label='Hora de Término', widget=forms.Select(choices=HOUR_CHOICES))
    address = forms.CharField(label='Endereço')
    min_age = forms.IntegerField(label='Idade Mínima Permitida')