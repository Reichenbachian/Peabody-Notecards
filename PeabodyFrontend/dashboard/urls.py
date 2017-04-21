from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'api/getSearchResults/$', views.getSearchResults),
	url(r'dashboard', views.index, name='index'),
	url(r'^$', views.index, name='index'),
]
