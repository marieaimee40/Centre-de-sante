from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class CategorieAgent(models.Model):
    id_categorie_agent=models.AutoField(primary_key=True)
    label=models.CharField(max_length=50)
    creation_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(blank=True, null=True)

class TypeActivite(models.Model):
    id_type_activite=models.AutoField(primary_key=True)
    label=models.CharField(max_length=50)
    creation_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(blank=True, null=True)

class Agent(models.Model):
    id_agent=models.AutoField(primary_key=True)
    code_agent=models.CharField(max_length=10)
    nom=models.CharField(max_length=50)
    prenoms=models.CharField(max_length=50)
    id_categorie_agent=models.ForeignKey(TypeActivite, on_delete=models.PROTECT)
    creation_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(blank=True, null=True)

class Periodicite(models.Model):
    id_periodicite=models.AutoField(primary_key=True)
    label=models.CharField(max_length=50)
    dim_date_column_name=models.CharField(max_length=20)
    creation_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(blank=True, null=True)

class Activite(models.Model):
    id_Activte=models.AutoField(primary_key=True)
    label=models.CharField(max_length=50)
    id_type_activite=models.ForeignKey(TypeActivite, on_delete=models.PROTECT)
    id_categorie_agent=models.ForeignKey(CategorieAgent, null=True, on_delete=models.SET_NULL)
    creation_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(blank=True, null=True)



class PeriodesReporting(models.Model): #a revoir(foreignkey)
    id_periodesreporting=models.AutoField(primary_key=True)
    id_activite=models.ForeignKey(Activite, on_delete=models.PROTECT)
    id_periodicite=models.ForeignKey(Periodicite, on_delete=models.PROTECT)
    creation_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(blank=True, null=True)

class DimDate(models.Model):
    id_date=models.AutoField(primary_key=True)

class Fact_Prestation(models.Model):
    id_fact_prestation=models.AutoField(primary_key=True)
    id_activite=models.ForeignKey(Activite, on_delete=models.PROTECT)
    id_date=models.ForeignKey(DimDate, on_delete=models.PROTECT)
    quantite=models.IntegerField()
    creation_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(blank=True, null=True)