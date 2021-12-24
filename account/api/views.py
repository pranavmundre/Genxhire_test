from rest_framework import generics, mixins, viewsets

from account.api.serializers import PersonSerializer, EmployeeSerializer
from account.models import Person, Employee


class PersonAPIView(generics.ListCreateAPIView, generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet, generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class EmployeeAPIView(generics.ListCreateAPIView, generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet, generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

