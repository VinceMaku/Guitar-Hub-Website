from django.conf.urls import url
from django.contrib import admin
from .views import(
	index,
	about,
	acoustic,
	electric,
	guitartuner,
)
app_name='html_tmplt'
urlpatterns=[
	url(r'^$', index, name='index'),
	url(r'^about/$', about, name='about'),
	url(r'^acoustic/$', acoustic, name='acoustic'),
	url(r'^electric/$', electric, name='electric'),
	url(r'^guitartuner$', guitartuner, name='guitartuner'),

]
