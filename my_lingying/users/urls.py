from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^feed',index, name='index'),
	url(r'^messaging', messaging, name='messaging'),

]