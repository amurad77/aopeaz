from cgitb import handler
from django.urls import path, include
from . import views

urlpatterns = [
    # path('tinymce/', include('tinymce.urls')),

    path('', views.index),
    path('partners/', views. partners, name='partners'),
    path('about/', views. about, name='about'),
    path('leadership/', views. leadership, name='leadership'),
    path('emin-aliyev/', views.emin, name='emin'),

]