from django.conf.urls import url
from cms import views

urlpatterns = [
    url('^$',views.lists),
    url('^detail/(\d+)/$',views.detail,name="detail_page"),
]