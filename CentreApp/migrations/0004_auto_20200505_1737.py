# Generated by Django 3.0.5 on 2020-05-05 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CentreApp', '0003_auto_20200505_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dimdate',
            name='jour',
        ),
        migrations.RemoveField(
            model_name='dimdate',
            name='semestre',
        ),
    ]
