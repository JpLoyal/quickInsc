from django import forms
from django.core.exceptions import ValidationError


class ParticipantForm(forms.Form):

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]

    ### Validadores 
    
    def validate_age(value):
        if not value >= 18:
            raise ValidationError("A idade ser maior que 18 anos.")

    name = forms.CharField(label='Nome', max_length=100)
    age = forms.IntegerField(label='Idade', required=False, validators=[validate_age])
    CPF = forms.CharField(label='CPF')
    gender = forms.ChoiceField(label='Sexo', choices=SEXO_CHOICES)
