from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead, \
                         current_datetime_template, more_current_datetime_template
from mysite.books.views import search
from mysite.contact.views import contact

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # mysite
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    ('^template_time/$', current_datetime_template),
    ('^more_time/$', more_current_datetime_template),

    # books
    (r'^search/$', search),

    # contact
    (r'^contact/$', contact),

    # admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

