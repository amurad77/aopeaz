from django.shortcuts import render
from core.models import Partner
# from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext_lazy as _
# from django.utils.translation import ugettext as _


# Create your views here.


def index(request):
    return render(request, 'index.html')

# def partners(request):
#     return render(request, 'partners.html')

def about(request):
    return render(request, 'about.html')

def leadership(request):
    return render(request, 'leadership.html')

def emin(request):
    return render(request, 'emin-aliyev.html')


def partners(request):
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

    return render(request, 'partners.html', context)