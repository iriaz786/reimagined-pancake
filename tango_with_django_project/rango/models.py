from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
class Category(models.Model):
        name = models.CharField(max_length=128, unique=True)
        views = models.IntegerField(default=0, unique=False)
        likes = models.IntegerField(default=0)
        slug = models.SlugField()

        def save(self, *args, **kwargs):
                # Uncomment if you don't want the slug to change every time the name changes
                #if self.id is None:
                        #self.slug = slugify(self.name)
                self.slug = slugify(self.name)
                super(Category, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0, unique=False)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title
class View(models.Model):
    number=models.IntegerField()
    def __unicode__(self):
      return self.number

class likes(models.Model):
    num=models.IntegerField()
    def __unicode__(self):
      return self.num

class Ox(models.Model):
    horn_length = models.IntegerField()

class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"      