from django.db import models
from ckeditor.fields import RichTextField


# id pass: sendmystuff

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField(blank=True, null=True)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='Blog/images',default='')

    def __str__(self):
        return self.title


class Site(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField(blank=True, null=True)

    # def __str__(self):
    #     return self.title

    def __str__(self):
        return self.title + " | " + str(self.pk)
