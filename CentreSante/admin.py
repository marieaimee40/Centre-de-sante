from django.contrib import admin
from .models import CategorieAgent
from .models import TypeActivite
from .models import Agent
from .models import Periodicite
from .models import Activite
from .models import PeriodesReporting
from .models import DimDate
from .models import Fact_Prestation

# Register your models here.

admin.site.register(CategorieAgent)
admin.site.register(TypeActivite)
admin.site.register(Agent)
admin.site.register(Periodicite)
admin.site.register(Activite)
admin.site.register(PeriodesReporting)
admin.site.register(DimDate)
admin.site.register(Fact_Prestation)