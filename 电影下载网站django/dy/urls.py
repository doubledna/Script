from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name = 'index' ),
    url(r'page/list_(\d+).html$', views.index, name = 'page'),
    url(r'movie/(\d+).html$', views.movie, name = 'movie'),
]
