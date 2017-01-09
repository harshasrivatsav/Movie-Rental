from django.conf.urls import url
from . import views

app_name = 'shopping'

urlpatterns = [
    url(r'^add/(?P<movie_id>[0-9]+)$', views.add, name='add'),
    url(r'^remove/(?P<movie_id>[0-9]+)$', views.remove, name='remove'),
    url(r'^show/$', views.show, name='show'),
    ]
