from django.conf.urls import url
from moneyflow import views
urlpatterns = [
    url(r'^mrecords/$', views.moneyflowrecord_list),
    url(r'^mrecords/(?P<pk>[0-9]+)/$', views.moneyflowrecord_detail),
]