from django.conf.urls import url
from . import views
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^wx$', views.wx, name='wx'),
]