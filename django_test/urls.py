"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from book import views as book_view
from contact import views as contact_view
from django.conf.urls import patterns, include
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^hello/$', views.hello),
    url('^current_datetime/$',views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$',views.hours_ahead),
    url('^current_datetime_template/$',views.current_datetime_template),
    url('^current_datetime_file/$',views.current_datetime_file),
    url('^current_datetime_render_response/$',views.current_datetime_render_response),
    url('^current_dateime_render_response_local/$',views.current_dateime_render_response_local),
    url('^trial_inheritance_render/$',views.trial_inheritance_render),
    url('^request_parameters/$',views.request_parameters),
    url('^search_form/$',book_view.search_form),
    url('^search/$',book_view.search),
    url('^contact/$',contact_view.contact),
#     url('^search/$','book.views.search'),
#     url('^arguments/(?P<year>\d{4})/(?P<month>\d{2})','contact.views.named_arguments_trial',{'template_name':'new_temlate.html'})
]

