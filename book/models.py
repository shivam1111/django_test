from __future__ import unicode_literals
from django.db import models

class Publisher(models.Model):
    #table name by default is appname_classname
    #in this case it will be book_publisher
    def __str__(self):
        return u'%s'%(self.name)

    class Meta:
        ordering = ['-id']
            
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

class Book(models.Model):
    title = models.CharField(max_length=100,verbose_name="Book Title")
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)    