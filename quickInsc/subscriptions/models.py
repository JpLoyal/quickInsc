from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    attractions = models.TextField(verbose_name='Atrações')
    description = models.TextField(verbose_name='Descrição')
    date = models.DateField(verbose_name='Data')
    time_starts = models.TimeField(verbose_name='Hora de Início')
    time_ends = models.TimeField(verbose_name='Hora de Término')
    address = models.CharField(verbose_name='Endereço', max_length=255, default='default')
    min_age = models.IntegerField(verbose_name='Idade Mínima')


class Participant(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    CPF = models.CharField(max_length=14, verbose_name='CPF')
    age = models.IntegerField(verbose_name='Idade')
    gender = models.CharField(max_length=1, verbose_name='Sexo')
    email = models.EmailField(max_length=255, verbose_name='E-mail')
    phone = models.CharField(max_length=20, verbose_name='Telefone')

    events = models.ManyToManyField(Event)