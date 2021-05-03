from django.db import models


# id pass : shane shane
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    subject = models.CharField(max_length=80, default="")
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=50)
    title_desc = models.TextField(max_length=100)

    image_one = models.ImageField(upload_to="About/images", default="")
    topic_one = models.CharField(max_length=50)

    topic_title = models.CharField(max_length=50)
    topic_desc = models.TextField(max_length=1000)

    image_two = models.ImageField(upload_to="About/images", default="")
    section = models.CharField(max_length=50)
    section_two = models.CharField(max_length=50)

    def __str__(self):
        return self.title + " | " + str(self.pk)


class MoreAbout(models.Model):
    title = models.CharField(max_length=50, default='')
    description = models.TextField(max_length=100, default='')

    def __str__(self):
        return self.title + " | " + str(self.pk)
