"""aope URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import index, partners, about, leadership, emin
# from news.views import news, news_details
from contact.views import contact, membership
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    # path('index1/', index1),
    path('index/', index),
    # path('news_detail/<slug:slug>/', news_details, name='news_details'),
    path('partners/', partners),
    path('about/', about),
    path('leadership/', leadership),
    path('emin-aliyev/', emin),
    # path('news/', news),
    path('contact/', contact),
    path('membership/', membership),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
