from django.db import models
from random import choices
from django.utils.translation import gettext_lazy as _



# Create your models here.

class Contact(models.Model):
    # information
    name = models.CharField('Ad Soyad', max_length = 20)
    number = models.CharField('Telefon nömrəsi', max_length = 20)
    email = models.EmailField('Email', max_length = 50)
    subject = models.CharField('Mövzu', max_length = 150)
    messege = models.TextField('Mesaj', max_length = 2000)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Membership(models.Model):
    GENDER_CHOICES = (
        ('M', _('Kişi')),
        ('F', _('Qadın'))
    )
    # information
    name = models.CharField('Ad', max_length = 256)
    surname = models.CharField('Soyad', max_length = 256)
    father_name = models.CharField('Ata adı', max_length = 256)
    gender = models.CharField('Cins', choices=GENDER_CHOICES, default='Male', max_length = 20)
    passport_number = models.CharField('Şəxsiyyət vəsiqəsinin seriya və nömrəsi', max_length = 20)
    passport_fin_number = models.CharField('Şəxsiyyət vəsiqəsinin indentifikasiya (FİN) kodu:', max_length = 20)
    born = models.DateField('Doğum tarixi')
    place_of_birth = models.CharField('Doğulduğu yer', max_length = 20)
    actual_residence = models.CharField('Faktiki yaşayış yeri', max_length = 256)
    home_phone_number = models.CharField('Ev nömrəsi', max_length = 20)
    phone_number = models.CharField('Mobil nömrə', max_length = 20)
    email = models.EmailField('Email', max_length = 256)
    areas_of_activity = models.CharField('Fəaliyyət istiqaməti', max_length = 5000)
    work_time = models.CharField('Qeyd etdiyi istiqamət üzrə bu müddətdir ki, fəaliyyət göstərir', max_length = 5000)
    establishment = models.CharField('Fəaliyyət istiqamətində təsisatın adı', max_length = 5000)
    adress = models.CharField('Təsisatın yerləşdiyi ünvan', max_length = 5000)
    facility_site = models.CharField('Təsisatın media və əlaqə vasitələri - Sayt', max_length = 50)
    facility_phone_number = models.CharField('Təsisatın media və əlaqə vasitələri - Telefon', max_length = 50)
    facility_mail = models.EmailField('Təsisatın media və əlaqə vasitələri - E-poçt', max_length = 50)
    project = models.TextField('Təsisat olaraq bu günə kimi qeyd edilən istiqamət üzrə hansı layihələri həyata keçirib', max_length = 5000)
    project_part = models.TextField('İcra etdiyim layihələrin hansı hissəsinin donor qurumlar və ya öz şəxsi hesabıma keçirilir', max_length = 5000)
    purpose = models.TextField('Sizə üzv olmaqda məqsəd və gözləntilərim', max_length = 5000)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name