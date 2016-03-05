from django.http import HttpResponse
from django.views import generic
from django.core.urlresolvers import reverse, reverse_lazy

from .models import Author

def index(request):
    return HttpResponse("Hello, world.")


class NewAuthorView(generic.CreateView):
    '''
    New author input view.
    '''
    model = Author
    fields = ['first_name', 'last_name']
    template_name = "pubman/author_edit.html"
    success_url = reverse_lazy('pubman:index')
