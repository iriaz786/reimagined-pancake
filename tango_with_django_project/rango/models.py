from django.db import models

# Create your models here.

from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(default=0)

    def save(self, *args, **kwargs):

    	self.slug = slugify(self.name)
    	super(Category, self).save(*args, **kwargs) 

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128, unique=True)
    url = models.URLField(max_length=255)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
    	self.slug=slugify(self.title)
    	super(Page, self).save(*args, **kwargs)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title



