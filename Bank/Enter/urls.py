from django.conf.urls import url
from Enter import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]
