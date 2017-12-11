from django.conf.urls import url

from . import views

app_name = 'bitprice'

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^monthly-records/(\w+)/$', views.monthly_records, name='monthly-records'),
]