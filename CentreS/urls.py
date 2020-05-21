"""CentreS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path,re_path
from rest_framework import permissions
from django.conf.urls import url, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#from rest_framework.documentation import include_docs_urls
schema_view = get_schema_view(
        openapi.Info(
        title="CentreApp API",
        default_version='v1'
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

from rest_framework import routers
from CentreApp.views import *


#urlpatterns = [
 #   path('admin/', admin.site.urls),
    #path('', include('CentreS.urls')),
 #   url(r'^api-auth/', include('rest_framework.urls')),
#]

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'Agent', AgentViewSet)
router.register(r'Categorie Agent', CategorieAgentViewSet)
router.register(r'Type Contact', TypeContactViewSet)
router.register(r'Type Activite', TypeActiviteViewSet)
router.register(r'Feedback Relance', FeedbackRelanceViewSet)
router.register(r'Patient', PatientViewSet)
router.register(r'Visite Patient', VisitePatientViewSet)
router.register(r'Relance Patient', RelancePatientViewSet)
router.register(r'Contact Patient', ContactPatientViewSet)
router.register(r'Personne Soutien', PersonneSoutienViewSet)
router.register(r'Activite',  ActiviteViewSet)
router.register(r'DimDate',  DimDateViewSet)
router.register(r'Fact Prestation',  FactPrestationViewSet)
router.register(r'Periodicite',  PeriodiciteViewSet)
router.register(r'Periode Reporting',  PeriodeReportingViewSet)
urlpatterns = router.urls

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^api/', include('rest_framework.urls')),
    url('api/', include(router.urls)),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
     #re_path(r'^doc(?P<format>\.json|\.yaml)$',
           # schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('api/doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'), 
]
#urlpatterns += router.urls
#if settings.DEBUG:
 #   from django.conf.urls.static import static
 #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 #   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)