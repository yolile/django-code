from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
 url(r'^$','principal.views.lista_bebidas'),
 url(r'^proyectos/','principal.views.lista_proyectos'),
 url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
 url(r'^admin/', include(admin.site.urls)),
)
