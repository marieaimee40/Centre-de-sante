from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class  CategorieAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model =  CategorieAgent
        fields = '__all__'

class  AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class  TypeContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeContact
        fields = '__all__'


class  TypeActiviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeActivite
        fields = '__all__'


class  FeedbackRelanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackRelance
        fields = '__all__'


class  PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class  VisitePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitePatient
        fields = '__all__'


class  RelancePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelancePatient
        fields = '__all__'


class  ContactPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPatient
        fields = '__all__'


class  PersonneSoutienSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonneSoutien
        fields = '__all__'


class  ActiviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activite
        fields = '__all__'


class  DimDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimDate
        fields = '__all__'

class  FactPrestationtSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactPrestation
        fields = '__all__'


class  PeriodiciteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodicite
        fields = '__all__'


class  PeriodeReportingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodeReporting
        fields = '__all__'
