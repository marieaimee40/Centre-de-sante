# Generated by Django 3.0.5 on 2020-05-04 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('id_Activte', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=50)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategorieAgent',
            fields=[
                ('id_categorie_agent', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=50)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DimDate',
            fields=[
                ('id_date', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Periodicite',
            fields=[
                ('id_periodicite', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=50)),
                ('dim_date_column_name', models.CharField(max_length=20)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeActivite',
            fields=[
                ('id_type_activite', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=50)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PeriodesReporting',
            fields=[
                ('id_periodesreporting', models.AutoField(primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('id_activite', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CentreSante.Activite')),
                ('id_periodicite', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CentreSante.Periodicite')),
            ],
        ),
        migrations.CreateModel(
            name='Fact_Prestation',
            fields=[
                ('id_fact_prestation', models.AutoField(primary_key=True, serialize=False)),
                ('quantite', models.IntegerField()),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('id_activite', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CentreSante.Activite')),
                ('id_date', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CentreSante.DimDate')),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id_agent', models.AutoField(primary_key=True, serialize=False)),
                ('code_agent', models.CharField(max_length=10)),
                ('nom', models.CharField(max_length=50)),
                ('prenoms', models.CharField(max_length=50)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('id_categorie_agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CentreSante.TypeActivite')),
            ],
        ),
        migrations.AddField(
            model_name='activite',
            name='id_categorie_agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CentreSante.CategorieAgent'),
        ),
        migrations.AddField(
            model_name='activite',
            name='id_type_activite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CentreSante.TypeActivite'),
        ),
    ]
