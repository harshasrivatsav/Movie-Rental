from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies/', include('movies.urls')),
    url(r'^', include('movies.urls')),
    url(r'^shopping-cart/', include('shopping.urls')),
]

