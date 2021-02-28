from django import forms
from .models import Checkout


class CheckoutForm(forms.ModelForm):
    num_title = forms.ChoiceField(
                widget = forms.Select(attrs={
                    'class': 'form-group',
                    'style': 'padding: 0 15px !important;',
                    
                }) , 
                choices = (
                    [('---', '---'),
                    ('050', '050'),
                    ('051', '051'),
                    ('055', '055'),
                    ('070', '070'),
                    ('077', '077'),
                    ('099', '099'),]
                ), initial='---', required = True,)
    class Meta:
        model = Checkout
        fields = (
            'name',
            'surname',
            'email',
            'num_title',
            'tel_number',
        )

        
        
    # def __init__(self, *args, **kwargs):
    #     super(CheckoutForm, self).__init__(*args, **kwargs)
    # # add custom error messages
    #     self.fields['num_title'].error_messages.update({
    #         'required': 'Operatoru bos qoymayin',
    #         'invalid': 'Operatoru bos qoymayin'

    #     })

        widgets = {
            
            'name': forms.TextInput(attrs={
                'class': 'form-group ',
                'placeholder': 'Ad '
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-group',
                'placeholder': 'Soyad '
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-group ',
                'placeholder': 'E-posta adresiniz'
            }),
            'tel_number': forms.NumberInput(attrs={
                'class': 'form-group',
                'placeholder': 'Mobil nömrə'
            }),
            

        }

        # error_messages = {
        #     'tel_number': {
        #         'required': "Thssas.",
        #         'invalid': "salam"
        #     },
        # }
