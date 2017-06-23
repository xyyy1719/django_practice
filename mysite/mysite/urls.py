"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from mysite.views import hello, current_datetime, hours_ahead, contact
from books import views
from mysite.ex.views import run_ex

time_patterns = [
    url(r'^$', current_datetime),
    url(r'^plus/(\d{1,2})/$', hours_ahead),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^time/', include(time_patterns)),
    url(r'^ex/(\d{1,2})/$', run_ex),
    url(r'^search/$', views.search),
    url(r'^contact/$', contact),
    url(r'^publishers/$', views.PublisherList.as_view())
]


