from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.contact_list, name='contact_list'),
    url(r'^details/(?P<pk>\d+)/$', views.contact_details, name='contact_details'),
    url(r'^remove/(?P<pk>\d+)/$', views.contact_rm, name='contact_rm'),
    url(r'^edit/(?P<pk>\d+)/$', views.contact_edit, name='contact_edit'),
    url(r'^create_new/$', views.contact_add, name='contact_add'),
    url(r'^remove_all/$', views.remove_all, name='remove_all'),
    url(r'^load_from_jsonplaceholder/$', views.load_from_json, name='load_from_jsonplaceholder')
]
