# Generated by Django 3.0.7 on 2020-10-03 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200929_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='pic',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='', upload_to='Blog/images'),
        ),
    ]
