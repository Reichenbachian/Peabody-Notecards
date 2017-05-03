from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'api/$', views.apiCall),
	url(r'dashboard', views.index, name='index'),
	url(r'^$', views.index, name='index'),
]
