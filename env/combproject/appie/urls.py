from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.seeschedule,name='seeschedule'),
    url(r'^createschedule',views.createschedule, name='createschedule'),
    ]