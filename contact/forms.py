from django import forms
from .models import Contact, Membership
# from django.utils.translation import gettext as _
from django.utils.translation import gettext as _

from django.forms.widgets import DateInput





class ContactForm(forms.ModelForm):

    class Meta:
 
        model = Contact
        fields = (
            'name',
            'number',
            'email',
            'subject',
            'messege',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Ad Soyadınız'),
                                    # 'id': 'value'
                                    
                                }),
            'number': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Telefon nömrəniz'),
                                    # 'id': 'value'
                                    
                                }),
            'email': forms.EmailInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Email ünvanınız'),
                                    # 'id': 'value1'
                                    
                                }),
            'subject': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Mövzu'),
                                    # 'id': 'value2'
                                }),
            'messege': forms.Textarea(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Mesajınız'),
                                    'cols': "30", 
                                    'rows': "10"
                                    # 'id': 'value3'
                                })
        }


class MembershipForm(forms.ModelForm):

    class Meta:
        GENDER_CHOICES = (
        ('M', 'Kişi'),
        ('F', 'Qadın')
    )
        model = Membership
        fields = (
            'name',
            'surname',
            'father_name',
            'gender',
            'passport_number',
            'passport_fin_number',
            'born',
            'place_of_birth',
            'actual_residence',
            'home_phone_number',
            'phone_number',
            'email',
            'areas_of_activity',
            'work_time',
            'establishment',
            'adress',
            'facility_site',
            'facility_phone_number',
            'facility_mail',
            'project',
            'project_part',
            'purpose'

        )
        widgets = {
            'name': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    # 'placeholder': 'Ad Soyadınız',
                                    # 'id': 'value'
                                    
                                }),

            'surname': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    # 'placeholder': 'Telefon nömrəniz',
                                    # 'id': 'value'
                                    
                                }),

            'father_name': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    # 'placeholder': 'Email ünvanınız',
                                    # 'id': 'value1'
                                    
                                }),

            'gender': forms.RadioSelect(attrs={
                                    'class': 'display',
                                }),

            'passport_number': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Məs: AZE12345678'),
                                }),

            'passport_fin_number': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Məs: 1234567'),
                                }),

            'born': DateInput(attrs={'type': 'date'}),

            'place_of_birth': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Məs: Azərbaycan, Bakı şəh.'),
                                }),

            'actual_residence': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Məs: Bakı şəh., Nərimanov ray.'),
                                }),

            'home_phone_number': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Məs: (+994 12) 999 99 99'),
                                }),

            'phone_number': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Məs: (+994 51) 999 99 99'),
                                }),

            'email': forms.EmailInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Məs: example@example.com'),
                                }),
            'areas_of_activity': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Məs: Orqanik sabun istehsalı'),
                                }),
            'work_time': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Məs: 1 il'),
                                }),
            'establishment': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Məs: XXX MMC, XXX İctimai Birliyi'),
                                }),
            'adress': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Məs: Bakı şəh., Nərimanov ray.'),
                                }),
            'facility_site': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Sayt'),
                                }),
            'facility_phone_number': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('Telefon'),
                                }),
            'facility_mail': forms.EmailInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': _('E-poçt'),
                                }),
            'project': forms.Textarea(attrs={
                                    'class': 'form-group ',
                                    # 'cols': 200,
                                    'rows': 3,
                                    # 'placeholder': 'Telefon',
                                }),
            'project_part': forms.Textarea(attrs={
                                    'class': 'form-group ',
                                    'rows': 3,
                                    # 'placeholder': 'Telefon',
                                }),
            'purpose': forms.Textarea(attrs={
                                    'class': 'form-group ',
                                    'rows': 3,
                                    # 'placeholder': 'Telefon',
                                }),
        }



