from django.conf.urls import url
from .views import login
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$',logout,name='logout', kwargs={'next_page': '/'}),
]