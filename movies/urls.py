from django.conf.urls import url
from . import views

app_name = 'movies'
urlpatterns = [
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^search/$', views.search, name='search'),
    url(r'^payment/$', views.payment, name='payment'),
    url(r'^success/$', views.success, name='success'),
    url(r'^news/$', views.news, name='news'),
    url(r'^newmovies/$', views.newmovies, name='newmovies'),
    ]