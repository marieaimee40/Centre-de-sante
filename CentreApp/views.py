from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializers import *

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class AgentViewSet(viewsets.ModelViewSet):

    queryset =Agent.objects.all()
    serializer_class = AgentSerializer

class CategorieAgentViewSet(viewsets.ModelViewSet):
    queryset = CategorieAgent.objects.all()
    serializer_class = CategorieAgentSerializer

class TypeContactViewSet(viewsets.ModelViewSet):
    queryset = TypeContact.objects.all()
    serializer_class = TypeContactSerializer


class TypeActiviteViewSet(viewsets.ModelViewSet):
    queryset = TypeActivite.objects.all()
    serializer_class = TypeActiviteSerializer


class FeedbackRelanceViewSet(viewsets.ModelViewSet):
    queryset = FeedbackRelance.objects.all()
    serializer_class = FeedbackRelanceSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class VisitePatientViewSet(viewsets.ModelViewSet):
    queryset = VisitePatient.objects.all()
    serializer_class = VisitePatientSerializer


class RelancePatientViewSet(viewsets.ModelViewSet):
    queryset = RelancePatient.objects.all()
    serializer_class = RelancePatientSerializer


class ContactPatientViewSet(viewsets.ModelViewSet):
    queryset = ContactPatient.objects.all()
    serializer_class = ContactPatientSerializer


class PersonneSoutienViewSet(viewsets.ModelViewSet):
    queryset = PersonneSoutien.objects.all()
    serializer_class = PersonneSoutienSerializer


class  ActiviteViewSet(viewsets.ModelViewSet):
    queryset =  Activite.objects.all()
    serializer_class =  ActiviteSerializer


class DimDateViewSet(viewsets.ModelViewSet):
    queryset = DimDate.objects.all()
    serializer_class = DimDateSerializer


class FactPrestationViewSet(viewsets.ModelViewSet):
    queryset = FactPrestation.objects.all()
    serializer_class = FactPrestationtSerializer


class PeriodiciteViewSet(viewsets.ModelViewSet):
    queryset = Periodicite.objects.all()
    serializer_class = PeriodiciteSerializer


class PeriodeReportingViewSet(viewsets.ModelViewSet):
    queryset = PeriodeReporting.objects.all()
    serializer_class = PeriodeReportingSerializer
