from django.conf.urls import url
from . import views

app_name='testapp'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^edit/$', views.edit, name='edit'),
	]