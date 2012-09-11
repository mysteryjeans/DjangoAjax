from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'django_ajax.views.home'),
    url(r'^gettime/$', 'django_ajax.views.gettime'),
    # Examples:
    # url(r'^$', 'django_ajax.views.home', name='home'),
    # url(r'^django_ajax/', include('django_ajax.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
