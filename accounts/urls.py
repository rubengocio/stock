from django.conf.urls import url
from .views import login, change_sucursal
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$',logout,name='logout', kwargs={'next_page': '/'}),
    url(r'^change_sucursal/$', change_sucursal, name='change_sucursal'),

]