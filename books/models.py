from django.db import models
from django.conf import settings
# Create your models here.
class Books(models.Model):
    bookID = models.CharField(max_length=30)
    title = models.CharField(max_length=60,)
    authors = models.CharField(max_length=60)
    average_rating = models.FloatField()
    isbn	= models.CharField(max_length=30,blank=True)
    isbn13	= models.CharField(max_length=30)
    language_code = models.CharField(max_length=30)  
    num_pages = models.IntegerField()
    ratings_count = models.IntegerField()
    text_reviews_count = models.IntegerField(blank=True)
    publication_date = models.DateField(blank=True)
    publisher = models.CharField(max_length=60)

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.isbn13, self.authors)
    # @property
    # def fields(self):
    #     return [f.name for f in self._meta.get_fields()]
