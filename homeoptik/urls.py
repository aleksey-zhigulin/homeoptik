"""homeoptik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
# from django.contrib.sitemaps.views import sitemap


from oscar.app import application
from oscar.views import handler500, handler404, handler403

from models import Subscription

from forked.newsletter_subscription.backend import ModelBackend
from forked.newsletter_subscription.urls import newsletter_subscriptions_urlpatterns


urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include(application.urls)),
    url(
        r'^newsletter/',
        include(newsletter_subscriptions_urlpatterns(
            backend=ModelBackend(Subscription),
        )),
    ),
    url(r'^help/contacts/$', 'homeoptik.views.email', name='contact'),
    # url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
                            url(r'^rosetta/', include('rosetta.urls')),
                            )

if settings.DEBUG:
    import debug_toolbar

    # Allow error pages to be tested
    urlpatterns += patterns('',
                            url(r'^403$', handler403),
                            url(r'^404$', handler404),
                            url(r'^500$', handler500),
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT}),
                            )
