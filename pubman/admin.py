from django.contrib import admin

from .models import Author
from .models import ConferenceSeries
from .models import Conference
from .models import Publication
from .models import Publisher
from .models import ProceedingsSeries

admin.site.register(Author)
admin.site.register(ConferenceSeries)
admin.site.register(Conference)
admin.site.register(Publication)
admin.site.register(Publisher)
admin.site.register(ProceedingsSeries)
