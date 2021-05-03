from django.db import models



class FormOne(models.Model):
    length = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(blank=True, default='')

    def __str__(self):
        return str(self.date)


class FormTwo(models.Model):
    name = models.TextField(max_length=200, null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=13, null=False)
    otp = models.CharField(max_length=6, null=False)

    # password = models.CharField(max_length=255, null=False)
    # company_name = models.TextField(max_length=200)

    def __str__(self):
        return self.phone
