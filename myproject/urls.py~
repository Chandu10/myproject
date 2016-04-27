from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^myapp/', include('myapp.urls')),
        url(r'^$', 'myapp.views.index'),
        url(r'^admin/', include(admin.site.urls)),
# user authentication urls
        url(r'^accounts/login/$', 'myapp.views.login'),
        url(r'^accounts/auth/$', 'myapp.views.auth_view'),
        url(r'^accounts/login/accounts/auth/$', 'myapp.views.auth_view'),
        url(r'^accounts/logout/$', 'myapp.views.logout'),
        url(r'^accounts/loggedin/$', 'myapp.views.loggedin'),
        url(r'^accounts/invalid/$', 'myapp.views.invalid_login'),
        url(r'^accounts/register/$', 'myapp.views.register_user'),
        url(r'^accounts/register_success/$', 'myapp.views.register_success'),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
         
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

