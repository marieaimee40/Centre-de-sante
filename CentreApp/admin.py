from django.contrib import admin
from .models import (
	CategorieAgent, TypeActivite, Agent, Activite, DimDate,
	FactPrestation, Periodicite, PeriodeReporting, Patient
	)

from reversion.admin import VersionAdmin

from import_export import resources
from import_export.admin import ImportExportModelAdmin



# Register your models here.


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
	list_display = ('code', 'nom', 'prenoms', 'date_enrolement', 'cohorte_actuelle',)


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
	list_display = ('date', 'jour', 'mois', 'nom_jour', 'nom_mois', 'semestre', 'annee',)



admin.site.register(CategorieAgent)
admin.site.register(TypeActivite)
#admin.site.register(Agent)

admin.site.register(Activite)

admin.site.register(DimDate, DimDateAdmin)
#admin.site.register(FactPrestation)

admin.site.register(Periodicite)
admin.site.register(PeriodeReporting)
