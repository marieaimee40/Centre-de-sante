import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator

# Create your models here.

class MonitoredTimeModel(models.Model):
	creation_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class CategorieAgent(MonitoredTimeModel):
	"""
	Le champ pour la categorie agent
	:param label: Un nom
	:type label: str
	:return: le nom de la categorie
	:rtype: str

	"""
	label = models.CharField(max_length=50, blank=False,help_text="Le nom de la categorie")
	

	def __str__(self):
		return self.label

	class Meta:
		verbose_name = "Categorie d'agents"
		verbose_name_plural = "Categories d'agents"

class TypeContact(MonitoredTimeModel):
	label = models.CharField(max_length=50, blank=False)

	def __str__(self):
		return self.label

	class Meta:
		verbose_name = "Type de contact"
		verbose_name_plural = "Types de contact"

class TypeActivite(MonitoredTimeModel):
	label = models.CharField(max_length=50, blank=False)

	def __str__(self):
		return self.label

	class Meta:
		verbose_name = "Type d'activites"
		verbose_name_plural = "Types d'activites"

class FeedbackRelance(models.Model):
	"""
	La reponse d'un patient suite en un appel ou le resultat de la relance 
	Exemple: Refus de venir ou Injoingable

	"""
	label = models.CharField("Retour de relance", max_length=20, blank=False)

	def __str__(self):
		return self.label

class Agent(MonitoredTimeModel):
	"""
	Enregistrement d'un agent qui exite sur le site ( code : code agent, nom, prenoms,et sa categorie agent)
	:model:'categorie_agent.CategorieAgent'
	"""
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
	date_enrolement = models.DateField(blank=False, validators = [MaxValueValidator(datetime.datetime.now().date())])
	

	def __str__(self):
		return self.code

	@property
	def cohorte_actuelle(self):
		today = datetime.datetime.now()
		diff_mois = (today.year - self.date_enrolement.year) *12 + today.month - self.date_enrolement.month + 1
		return "M{}".format(str(diff_mois))

	@property
	def derniere_visite(self):
		return self.visites_patients.latest('creation_time')

	@property
	def derniere_relance(self):
		return self.relances_patients.latest('creation_time')

	@property
	def liste_contacts_actifs(self):
		return ", ".join(["{} : {}".format(contact["type_contact__label"], contact["contact"]) for contact in list(self.contacts_patients.filter(active=True).values('type_contact__label','contact'))])

class VisitePatient(MonitoredTimeModel):
	patient = models.ForeignKey("Patient", on_delete=models.CASCADE, blank=True, null=True, related_name="visites_patients")
	activite = models.ForeignKey("Activite", on_delete=models.CASCADE, blank=True, null=True, help_text="Activité réalisée", related_name="visites_patients")
	date = models.DateField("Date de la visite")

	def __str__(self):
		return "{}: {}".format(self.date, self.activite)

class RelancePatient(MonitoredTimeModel):
	patient = models.ForeignKey("Patient", on_delete=models.CASCADE, blank=True, null=True, related_name="relances_patients")
	date = models.DateField("Date de la visite")
	feedback = models.ForeignKey("FeedbackRelance", on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return "{}: {}".format(self.date, self.feedback)
	
class ContactPatient(MonitoredTimeModel):
	patient = models.ForeignKey("Patient", on_delete=models.CASCADE, blank=True, null=True, related_name="contacts_patients")
	type_contact = models.ForeignKey("TypeContact", on_delete=models.SET_NULL, blank=True, null=True)
	contact = models.CharField("Contact", max_length=50, blank=False, null=False)

	active = models.BooleanField("Contact actif", default=True)

	def __str__(self):
		return self.contact
	
	@property
	def description(self):
		return 


class PersonneSoutien(MonitoredTimeModel):
	patient = models.ForeignKey("Patient", on_delete=models.CASCADE, blank=True, null=True)
	nom = models.CharField(max_length=50, blank=False)
	prenoms = models.CharField(max_length=50, blank=True, null=True)
	contact = models.CharField("Contact", max_length=50, blank=False, null=False)

	def __str__(self):
		return "{} {}".format(self.prenoms, self.nom.upper())

class Activite(MonitoredTimeModel):
	label = models.CharField(max_length=50, blank=False)
	type_activite = models.ForeignKey("TypeActivite", on_delete = models.PROTECT, related_name="activites")
	categorie_agent = models.ForeignKey("CategorieAgent", null=True, on_delete = models.SET_NULL, related_name="activites")

	def __str__(self):
		return self.label

class DimDate(MonitoredTimeModel):
	date = models.DateField(primary_key=True, unique=True, blank=False)

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
