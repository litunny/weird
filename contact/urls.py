from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<pk>\d+)/$', views.contact_view, name="contact_view"),
    url(r'^new/$', views.contact_new, name="contact_new"),
    url(r'^edit/(?P<pk>\d+)$', views.contact_edit, name="contact_edit"),
]