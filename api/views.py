from django.shortcuts import render

from rest_framework import viewsets

import django_filters
from rest_framework import filters

from .serializers import LocationSerializer
from .serializers import FlatSerializer
from .serializers import RoomSerializer
from .serializers import StaffSerializer
from .serializers import ResidentSerializer
from .serializers import EnquireSerializer
from .serializers import ReportSerializer

from .models import Location
from .models import Flat
from .models import Room
from .models import Report

from .models import Resident
from .models import Staff
from .models import Enquire

# Filter classes
class EnquireFilter(filters.FilterSet):
    status = django_filters.CharFilter(name="status__id")
    class Meta:
        model = Enquire
        fields = ['reference', 'status']

class ReportFilter(filters.FilterSet):
    status = django_filters.CharFilter(name="status__id")
    class Meta:
        model = Report
        fields = ['reference', 'status']

class StaffFilter(filters.FilterSet):
    first_name = django_filters.CharFilter(name="user__first_name")
    last_name = django_filters.CharFilter(name="user__last_name")
    email = django_filters.CharFilter(name="user__email")
    role = django_filters.CharFilter(name="role__id")

    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'email', 'role']

class EnquireViewSet(viewsets.ModelViewSet):
    queryset         = Enquire.objects.all()
    serializer_class = EnquireSerializer
    filter_backends  = (filters.DjangoFilterBackend,filters.OrderingFilter)
    filter_class     = EnquireFilter
    ordering_fields = ('created_at', 'status')
    ordering = ('created_at')

class ReportViewSet(viewsets.ModelViewSet):
    queryset         = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends  = (filters.DjangoFilterBackend,filters.OrderingFilter)
    filter_class     = ReportFilter
    ordering_fields = ('created_at', 'status')
    ordering = ('-created_at','status')

class LocationViewSet(viewsets.ModelViewSet):
    queryset         = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends  = (filters.DjangoFilterBackend,)
    filter_fields    = ('postal', 'city', 'address', 'building')

class FlatViewSet(viewsets.ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
    filter_backends  = (filters.DjangoFilterBackend,)
    filters_fields   = ('identificator', 'location',)

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filter_backends  = (filters.DjangoFilterBackend,)
    filter_class     = StaffFilter

class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    filter_backends  = (filters.DjangoFilterBackend,)
    # filter_class     = ResidentFilter