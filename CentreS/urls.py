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
from django.urls import path
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Swagger API')

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
router.register(r'CategorieAgent', CategorieAgentViewSet)
router.register(r'TypeContact', TypeContactViewSet)
router.register(r'TypeActivite', TypeActiviteViewSet)
router.register(r'FeedbackRelance', FeedbackRelanceViewSet)
router.register(r'Patient', PatientViewSet)
router.register(r'VisitePatient', VisitePatientViewSet)
router.register(r'RelancePatient', RelancePatientViewSet)
router.register(r'ContactPatient', ContactPatientViewSet)
router.register(r'PersonneSoutien', PersonneSoutienViewSet)
router.register(r'Activite',  ActiviteViewSet)
router.register(r'DimDate',  DimDateViewSet)
router.register(r'FactPrestation',  FactPrestationViewSet)
router.register(r'Periodicite',  PeriodiciteViewSet)
router.register(r'PeriodeReporting',  PeriodeReportingViewSet)
urlpatterns = router.urls

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    #url(r'^docs/', schema_view),
    #url(r'^api-auth/', include('rest_framewosrk_swagger.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)