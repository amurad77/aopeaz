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

    return render(request, 'partners.html')