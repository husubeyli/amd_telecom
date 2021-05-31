from django import forms
# from typing_extensions import Required
from .models import Order
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class CheckoutForm(forms.ModelForm):
    # num_title = forms.ChoiceField(
    #             widget = forms.Select(attrs={
    #                 'class': 'form-group form-control form-select',
    #                 'style': 'padding: 0 15px !important;',
    #                 'required': 'true'
        
    #             }) , 
    #             choices = (
    #                 [('---', '---'),
    #                 ('050', '050'),
    #                 ('051', '051'),
    #                 ('055', '055'),
    #                 ('070', '070'),
    #                 ('077', '077'),
    #                 ('099', '099'),]
    #             ), initial='---', required = True,)
    
    # phone_number = PhoneNumberField(
    #     widget = PhoneNumberPrefixWidget(initial='AZ')
    # )        
    # attrs={'class': 'form-group form-control form-select', 'required': 'true'},

    class Meta:
        model = Order
        fields = (
            'name',
            'surname',
            'email',
            # 'num_title',
            'tel_number',
            'message',
        )
        requured = (
            'name',
            'surname',
            'email',
            # 'num_title',
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
                'class': 'form-control form-name',
                "type":"text",
                'placeholder': 'Adınızı daxil edin',
                'minlength':"3",
                'maxlegth':"20",
                'required': True
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control form-surname',
                'placeholder': 'Soyadınızı daxil edin',
                'minlength':"3",
                'maxlegth':"20",
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-email',
                'type': 'email',
                'placeholder': 'E-poçt adresinizi daxil edin',
                'minlength': "3",
                'maxlegth': "20",
                'required': True
            }),
            'tel_number': forms.NumberInput(attrs={
                'class': 'form-control form-number',
                'type': 'tel',
                'placeholder': 'Nömrənizi daxil edin',
                # 'minlength': "10",
                # 'maxlegth': "10",
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': '  Sifariş etdiyiniz məhsul haqqında qeydləriniz varsa yazın',
                'rows': 6,
            })
        }
        # labels = {
            # 'first_name': 'Ad',
            # 'last_name': 'Soyad',
            # 'phone_number': 'Əlaqə nomrəsi',
            # 'email': 'Elektron poçt ünvanı',
            # 'message': 'İsmarıc'
        # }

        # error_messages = {
        #     'tel_number': {
        #         'required': "Thssas.",
        #         'invalid': "salam"
        #     },
        # }
