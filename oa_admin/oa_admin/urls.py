from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oa_admin.views.home', name='home'),
    # url(r'^oa_admin/', include('oa_admin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    (r'^uploads/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_PATH}),
)
