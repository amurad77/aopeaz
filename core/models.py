from statistics import mode
from django.db import models
from django.urls import reverse
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

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return self.name


class PartnerCategory(models.Model):
    # information
    name = models.CharField('Partnyor kateqoriyası', max_length = 20)

    def __str__(self):
        return self.name

class Partner(models.Model):
    #realtion
    partner = models.ForeignKey(PartnerCategory, on_delete=models.CASCADE)

    # information
    name = models.CharField('Ad', max_length = 20)
    logo = models.ImageField("Logo", upload_to='media/partners_images')

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


