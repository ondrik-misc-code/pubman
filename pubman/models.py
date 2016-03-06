from django.db import models


###############################################################################
class Author(models.Model):
    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        '''
        Conversion to a string.
        '''
        return self.first_name + " " + self.last_name


###############################################################################
class Publisher(models.Model):
    name = models.CharField(max_length=128)


###############################################################################
class ProceedingsSeries(models.Model):
    name = models.CharField(max_length=256)
    abbr = models.CharField(max_length=128, null=True)


###############################################################################
class ConferenceSeries(models.Model):
    # name of the conference series
    name = models.TextField()
    # abbreviation
    abbr = models.CharField(max_length=128, null=True)

    def __str__(self):
        '''
        Conversion to a string.
        '''
        return self.abbr + "---" + self.name


###############################################################################
class Conference(models.Model):
    # series of the conference
    conf_series = models.ForeignKey(ConferenceSeries, on_delete=models.SET_NULL, null=True)
    # year of the conference
    year = models.IntegerField(null=True)
    # the run number of the conference
    run_num = models.IntegerField(null=True)
    # proceedings were published in series ...
    published_in = models.ForeignKey(ProceedingsSeries, on_delete=models.SET_NULL, null=True)
    # the volume of a notes series proceedings were published in
    published_in_vol = models.IntegerField(null=True)


###############################################################################
class Publication(models.Model):
    # title of the contribution
    title = models.TextField()
    # appeared in conference?
    conference = models.ForeignKey(Conference, on_delete=models.SET_NULL, null=True)
    # authors
    authors = models.ManyToManyField(Author, through="AuthorOf")


###############################################################################
class AuthorOf(models.Model):
    # author
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # publication
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    # order of the author
    order = models.IntegerField(null=True)
