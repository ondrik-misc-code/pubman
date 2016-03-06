from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Author
from .models import ConferenceSeries
from .models import Conference

##############################################################################
def index(request):
    '''
    The index page.
    '''
    return render(request, "pubman/index.html")

##############################################################################
class AuthorList(generic.ListView):
    '''
    List of authors.
    '''
    model = Author
    template_name = "pubman/author_list.html"
    context_object_name = "author_list"


##############################################################################
class NewAuthorView(generic.CreateView):
    '''
    New author input view.
    '''
    model = Author
    fields = ['first_name', 'last_name']
    template_name = "pubman/author_new.html"
    success_url = reverse_lazy('pubman:author_list')


##############################################################################
class EditAuthorView(generic.UpdateView):
    '''
    View for editing an author.
    '''
    model = Author
    fields = ['first_name', 'last_name']
    template_name = "pubman/author_edit.html"
    success_url = reverse_lazy('pubman:author_list')


##############################################################################
class DeleteAuthorView(generic.DeleteView):
    '''
    View for deleting an author.
    '''
    model = Author
    template_name = "pubman/author_delete.html"
    success_url = reverse_lazy('pubman:author_list')


##############################################################################
class ConferenceSeriesList(generic.ListView):
    '''
    List of conference series.
    '''
    model = ConferenceSeries
    template_name = "pubman/conference_series_list.html"
    context_object_name = "series_list"


##############################################################################
class NewConferenceSeriesView(generic.CreateView):
    '''
    New conference series input view.
    '''
    model = ConferenceSeries
    fields = ['abbr', 'name']
    template_name = "pubman/conference_series_new.html"
    success_url = reverse_lazy('pubman:conference_series_list')


##############################################################################
class EditConferenceSeriesView(generic.UpdateView):
    '''
    View for editing conference series.
    '''
    model = ConferenceSeries
    fields = ['abbr', 'name']
    template_name = "pubman/conference_series_edit.html"
    success_url = reverse_lazy('pubman:conference_series_list')


##############################################################################
class DeleteConferenceSeriesView(generic.DeleteView):
    '''
    View for deleting conference series.
    '''
    model = ConferenceSeries
    template_name = "pubman/conference_series_delete.html"
    success_url = reverse_lazy('pubman:conference_series_list')


##############################################################################
class ConferenceList(generic.ListView):
    '''
    List of conferences.
    '''
    model = Conference
    template_name = "pubman/conference_list.html"
    context_object_name = "conference_list"


##############################################################################
class NewConferenceView(generic.CreateView):
    '''
    New conference input view.
    '''
    model = Conference
    fields = ['conf_series', 'year']
    template_name = "pubman/conference_new.html"
    success_url = reverse_lazy('pubman:conference_list')

    # def __init__(self):
    #     '''
    #     Constructor of the view that fills the conference series.
    #     '''
    #     fields['series'].queryset = ConferenceSeries


##############################################################################
class EditConferenceView(generic.UpdateView):
    '''
    View for editing a conference.
    '''
    model = Conference
    fields = ['conf_series.abbr', 'year']
    template_name = "pubman/conference_edit.html"
    success_url = reverse_lazy('pubman:conference_list')


##############################################################################
class DeleteConferenceView(generic.DeleteView):
    '''
    View for deleting conferences.
    '''
    model = Conference
    template_name = "pubman/conference_delete.html"
    success_url = reverse_lazy('pubman:conference_list')
