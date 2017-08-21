from django.conf.urls import url

from map_search import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

]
