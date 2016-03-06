from django.conf.urls import url

from . import views

app_name = 'pubman'
urlpatterns = [

    # Top
    url(r'^$', views.index, name='index'),

    # Authors
    url(r'^authors/$', views.AuthorList.as_view(), name='author_list'),
    url(r'^authors/new/$', views.NewAuthorView.as_view(), name='author_new'),
    url(r'^authors/(?P<pk>[0-9]+)/edit/$', views.EditAuthorView.as_view(), name='author_edit'),
    url(r'^authors/(?P<pk>[0-9]+)/delete/$', views.DeleteAuthorView.as_view(), name='author_delete'),

    # Conference series
    url(r'^conference_series/$', views.ConferenceSeriesList.as_view(), name='conference_series_list'),
    url(r'^conference_series/new/$', views.NewConferenceSeriesView.as_view(), name='conference_series_new'),
    url(r'^conference_series/(?P<pk>[0-9]+)/edit/$', views.EditConferenceSeriesView.as_view(), name='conference_series_edit'),
    url(r'^conference_series/(?P<pk>[0-9]+)/delete/$', views.DeleteConferenceSeriesView.as_view(), name='conference_series_delete'),

    # Conferences
    url(r'^conferences/$', views.ConferenceList.as_view(), name='conference_list'),
    url(r'^conferences/new/$', views.NewConferenceView.as_view(), name='conference_new'),
    url(r'^conferences/(?P<pk>[0-9]+)/edit/$', views.EditConferenceView.as_view(), name='conference_edit'),
    url(r'^conferences/(?P<pk>[0-9]+)/delete/$', views.DeleteConferenceView.as_view(), name='conference_delete'),
]
