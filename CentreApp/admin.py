from django.contrib import admin
from .models import *

from reversion.admin import VersionAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin


admin.site.site_header = "Compteur d'activites"
admin.site.site_title = "Compteur d'activites"
#admin.site.index_title = "Index title"
# Register your models here.



class VisitePatientInline(admin.TabularInline):
    model = VisitePatient

class RelancePatientInline(admin.TabularInline):
    model = RelancePatient

class ContactPatientInline(admin.TabularInline):
    model = ContactPatient

class PersonneSoutienInline(admin.TabularInline):
    model = PersonneSoutien




class AgentResource(resources.ModelResource):
	class Meta:
		model = Agent
		import_id_fields = ('code',)
		exclude = ('id', 'creation_time', 'update_time', )

@admin.register(Agent)
class AgentAdmin(ImportExportModelAdmin, VersionAdmin):
    	resource_class = AgentResource


class PatientResource(resources.ModelResource):
	class Meta:
		model = Patient
		import_id_fields = ('code',)
		exclude = ('id', 'creation_time', 'update_time', )

@admin.register(Patient)
class PatientAdmin(ImportExportModelAdmin, VersionAdmin):
	resource_class = PatientResource
	list_display = ('code', 'nom', 'prenoms', 'date_enrolement', 'liste_contacts_actifs', 'cohorte_actuelle','derniere_visite', 'derniere_relance')

	inlines = [
		VisitePatientInline,
		RelancePatientInline,
		ContactPatientInline,
		PersonneSoutienInline,
	]

@admin.register(FactPrestation)
class FactPrestationAdmin(VersionAdmin):
	pass

class DimDateResource(resources.ModelResource):
	class Meta:
		model = DimDate
		import_id_fields = ('date',)
		exclude = ('creation_time', 'update_time', )

class DimDateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = DimDateResource
	list_display = ('date', 'jour', 'mois', 'nom_jour', 'nom_mois', 'trimestre', 'semestre', 'annee',)


admin.site.register(CategorieAgent)
admin.site.register(TypeActivite)
admin.site.register(TypeContact)
admin.site.register(FeedbackRelance)
admin.site.register(Activite)
admin.site.register(DimDate, DimDateAdmin)
admin.site.register(Periodicite)
admin.site.register(PeriodeReporting)
