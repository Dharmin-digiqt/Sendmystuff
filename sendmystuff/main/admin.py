from django.contrib import admin
from .models import Contact, About, MoreAbout

# Register your models here.

admin.site.register(Contact)
admin.site.register(About)
admin.site.register(MoreAbout)
