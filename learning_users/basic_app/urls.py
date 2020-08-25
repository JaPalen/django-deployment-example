from django.conf.urls import url
from basic_app import views
from django.urls import path, include, re_path

#TEMPLATE URLs
app_name = 'basic_app'

urlpatterns = [
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^userLogin/$',views.userLogin,name='userLogin'),
]
