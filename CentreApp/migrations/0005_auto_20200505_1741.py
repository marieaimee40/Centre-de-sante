# Generated by Django 3.0.5 on 2020-05-05 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CentreApp', '0004_auto_20200505_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dimdate',
            name='annee',
        ),
        migrations.RemoveField(
            model_name='dimdate',
            name='semaine',
        ),
        migrations.RemoveField(
            model_name='dimdate',
            name='trimestre',
        ),
    ]
