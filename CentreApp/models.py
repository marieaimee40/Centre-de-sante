from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime

# Create your models here.

class MonitoredTimeModel(models.Model):
	creation_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class CategorieAgent(MonitoredTimeModel):
	label = models.CharField(max_length=50, blank=False)

	def __str__(self):
		return self.label

	class Meta:
		verbose_name = "Categorie d'agents"
		verbose_name_plural = "Categories d'agents"

class TypeActivite(MonitoredTimeModel):
	label = models.CharField(max_length=50, blank=False)

	def __str__(self):
		return self.label

	class Meta:
		verbose_name = "Type d'activites"
		verbose_name_plural = "Types d'activites"

class Agent(MonitoredTimeModel):
	code = models.CharField(max_length=10, blank=False)
	nom = models.CharField(max_length=50, blank=False)
	prenoms = models.CharField(max_length=50, blank=True, null=True)
	categorie_agent = models.ForeignKey("CategorieAgent", on_delete = models.PROTECT, related_name="agents")

	def __str__(self):
		return "{} {}".format(self.prenoms, self.nom)

class Patient(MonitoredTimeModel):
	code = models.CharField(max_length=10, blank=False)
	nom = models.CharField(max_length=50, blank=False)
	prenoms = models.CharField(max_length=50, blank=True, null=True)
	date_enrolement = models.DateField(blank=False)

	def __str__(self):
		return "{} {}".format(self.prenoms, self.nom)

	@property
	def cohorte_actuelle(self):
		today = datetime.datetime.now()
		diff_mois = (today.year - self.date_enrolement.year) *12 + today.month - self.date_enrolement.month + 1
		return "M-{}".format(str(diff_mois))


class Activite(MonitoredTimeModel):
	label = models.CharField(max_length=50, blank=False)
	type_activite = models.ForeignKey("TypeActivite", on_delete = models.PROTECT, related_name="activites")
	categorie_agent = models.ForeignKey("CategorieAgent", null=True, on_delete = models.SET_NULL, related_name="activites")

	def __str__(self):
		return self.label

class DimDate(MonitoredTimeModel):
	date = models.DateField(primary_key=True, unique=True, blank=False)
	#jour = models.PositiveIntegerField(blank=False)
	#semaine = models.PositiveIntegerField(blank=False)
	#mois = models.PositiveIntegerField(blank=False)
	#trimestre = models.PositiveIntegerField(blank=False)
	#semestre = models.PositiveIntegerField(blank=False)
	#annee = models.PositiveIntegerField(blank=False)

	class Meta:
		verbose_name = "Dimension DATE"
		verbose_name_plural = "Dimensions DATE"

	@property
	def jour(self):
		return str(self.date.day)

	@property
	def mois(self):
		return str(self.date.month)

	@property
	def semaine(self):
		return str(self.date.strftime("%V"))

	@property
	def nom_jour(self):
		return str(self.date.strftime("%A"))

	@property
	def nom_mois(self):
		return str(self.date.strftime("%B"))

	@property
	def trimestre(self):
		return str(int(self.date.month/3)+1)

	@property
	def semestre(self):
		return str(int(self.date.month/6)+1)

	@property
	def annee(self):
		return str(self.date.year)


class FactPrestation(MonitoredTimeModel):
	activite = models.ForeignKey("Activite", on_delete = models.PROTECT, related_name="prestations")
	date = models.ForeignKey("DimDate", on_delete = models.PROTECT, related_name="prestations")
	quantite = models.IntegerField(blank=False)

	class Meta:
		verbose_name = "Prestation"
		verbose_name_plural = "Prestations"

class Periodicite(MonitoredTimeModel):
	label = models.CharField(max_length=50, blank=False)
	dim_date_column_name = models.CharField(max_length=20, blank=False)

	def __str__(self):
		return self.label

class PeriodeReporting(MonitoredTimeModel):
	activite = models.ForeignKey("Activite", on_delete = models.PROTECT, related_name="periodes_reporting")
	periodicite = models.ForeignKey("Periodicite", on_delete = models.PROTECT, related_name="periodes_reporting")

	class Meta:
		verbose_name = "Periode de reporting"
		verbose_name_plural = "Periodes de reporting"
