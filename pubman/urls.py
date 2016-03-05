from django.conf.urls import url

from . import views

app_name = 'pubman'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^authors/new/$', views.NewAuthorView.as_view(), name='new_author'),
]
