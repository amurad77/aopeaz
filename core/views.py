import imp
from django.shortcuts import render
from core.models import Partner
# Create your views here.

def index(request):
    partner_dovlet = Partner.objects.filter(partner__name__contains='Dövlət qurumları').order_by('-id')
    partner_beynelxalq = Partner.objects.filter(partner__name__contains='Beynəlxalq qurumlar').order_by('-id')
    partner_yerli = Partner.objects.filter(partner__name__contains='Yerli şirkətlər').order_by('-id')
    partner_xarici = Partner.objects.filter(partner__name__contains='Xarici şirkətlər').order_by('-id')
    partner_assosiasiyalar = Partner.objects.filter(partner__name__contains='Assosiasiyalar').order_by('-id')


    context = {
        'partner_dovlet': partner_dovlet,
        'partner_beynelxalq': partner_beynelxalq,
        'partner_yerli': partner_yerli,
        'partner_xarici': partner_xarici,
        'partner_assosiasiyalar': partner_assosiasiyalar
    }

    return render(request, 'index.html', context)