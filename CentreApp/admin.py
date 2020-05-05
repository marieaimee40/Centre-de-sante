from django.contrib import admin
from .models import CategorieAgent, TypeActivite, Agent, Activite, DimDate, FactPrestation, Periodicite, PeriodeReporting

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

@admin.register(FactPrestation)
class FactPrestationAdmin(VersionAdmin):
	pass



class DimDateAdmin(admin.ModelAdmin):
	list_display = ('date', 'jour', 'mois', 'semestre', 'annee',)



admin.site.register(CategorieAgent)
admin.site.register(TypeActivite)
#admin.site.register(Agent)

admin.site.register(Activite)

admin.site.register(DimDate, DimDateAdmin)
#admin.site.register(FactPrestation)

admin.site.register(Periodicite)
admin.site.register(PeriodeReporting)
