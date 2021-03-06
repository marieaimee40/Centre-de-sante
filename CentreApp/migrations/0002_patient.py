# Generated by Django 3.0.5 on 2020-05-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CentreApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=10)),
                ('nom', models.CharField(max_length=50)),
                ('prenoms', models.CharField(blank=True, max_length=50, null=True)),
                ('date_enrolement', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
