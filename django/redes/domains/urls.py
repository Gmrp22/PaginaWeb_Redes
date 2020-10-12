from django.conf.urls import url
from . import views

app_name = 'domains'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^domains/$', views.dominios, name='dominios'),
    url(r'^new_domain/$', views.createDominio, name='create_domain'),
]
