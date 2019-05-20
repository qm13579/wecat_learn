from django.urls import path
from api import views
from django.conf.urls import url
urlpatterns = [

    url('^$',views.index,name='index'),
    url('login',views.login,name='login'),
    url(r'^change/(\d+)$',views.change,name='change')
    # url(r'^delete/(\d+)$',views.change,name='change')

]