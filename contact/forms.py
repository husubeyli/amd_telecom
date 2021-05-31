from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets

from .models import Contact


class ContactForm(forms.ModelForm):


    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'message'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': "form-control",
                'id': "name",
                'placeholder': "Adınızı daxil edin *",
                'maxlength': 50,
                'required': True
            }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control",
                'id': "last-name",
                'placeholder': "Soyadınızı daxil edin *",
                'maxlength': 50,
                'required': True
            }),
            'phone_number': forms.TextInput(attrs={
                'class': "form-control",
                'id': "review",
                'placeholder': "Əlaqə nomrənızı daxil edin *",
                'maxlength': 13,
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'id': "email",
                'placeholder': "Elektron poçt ünvanınızı daxil edin *",
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': "form-control",
                'id': "exampleFormControlTextarea1",
                'placeholder': "Mesajınızı daxil edin...",
                'rows': 6,
                'required': True
            })

        }
        labels = {
            'first_name': 'Ad',
            'last_name': 'Soyad',
            'phone_number': 'Əlaqə nomrəsi',
            'email': 'Elektron poçt ünvanı',
            'message': 'Mesaj'
        }
        error_messages = {
            'phone_number': {
                # 'required': "This writer's name is too long.",
                'invalid': 'Düzgün bir telefon nömrəsi daxil edin (məs. (012) 312 34 56) və ya beynəlxalq zəng prefiksi olan bir nömrə daxil edin.'
            },
        }
