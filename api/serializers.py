from rest_framework import serializers

from .models import Room
from .models import Flat
from .models import Location
from .models import Role
from .models import Enquire
from .models import Report
from .models import Status

from django.contrib.auth.models import User
from .models import Resident
from .models import Staff

# Custom Fields
class StatusField(serializers.RelatedField):
    queryset = Status.objects.all()

    def to_representation(self, data):
        return '%s' % (data.title)
    def to_internal_value(self, data):
        return Status.objects.get(id=data)

class EnquireField(serializers.RelatedField):
    def to_representation(self, data):
        return '%s' % (data.title)
    def to_internal_value(self, data):
        return Status.objects.get(id=data)

class RoomSerializer(serializers.ModelSerializer):
    flat     = serializers.SlugRelatedField(many=False, read_only=True, slug_field='identificator')
    # resident = serializers.HyperlinkedRelatedField(many=False, view_name='resident-detail', read_only=True)

    class Meta:
        model  = Room
        fields = ('flat', 'identificator')
        # fields = ('flat', 'identificator', 'resident')

class FlatSerializer(serializers.ModelSerializer):
    location = serializers.HyperlinkedRelatedField(many=False, view_name='location-detail', read_only=True)
    rooms = serializers.HyperlinkedRelatedField(many=True, view_name='room-detail', read_only=True)
    # rooms = RoomSerializer(many=True, read_only=True)
    
    class Meta:
        model = Flat
        fields = ('identificator', 'location', 'rooms')

class LocationSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('postal', 'city', 'address', 'building')

class LocationSerializer(serializers.ModelSerializer):
    flats = serializers.HyperlinkedRelatedField(many=True, view_name='flat-detail', read_only=True)
    enquires = serializers.HyperlinkedRelatedField(many=True, view_name='enquire-detail', read_only=True)
    class Meta:
        model = Location
        fields = ('postal', 'city', 'address', 'building', 'flats', 'enquires')

# Staff Serializers

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('title', 'level')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class StaffSerializer(serializers.ModelSerializer):
    role = serializers.SlugRelatedField(many=False, read_only=True, slug_field='title')
    reports = serializers.HyperlinkedRelatedField(many=True, view_name='report-detail', read_only=True)
    user = UserSerializer(many=False)
    class Meta:
        model = Staff
        fields = ('phone', 'role', 'user', 'reports')

class ResidentSerializer(serializers.ModelSerializer):
    room = RoomSerializer(many=False)
    user = UserSerializer(many=False)
    class Meta:
        model = Resident
        fields = ('phone', 'room', 'user')

class EnquireSerializer(serializers.ModelSerializer):
    status   = StatusField(read_only=False)
    location = LocationSimpleSerializer(many=False)
    resident = ResidentSerializer(many=False)
    reports  = serializers.HyperlinkedRelatedField(many=True, view_name='report-detail', read_only=True)

    class Meta:
        model = Enquire
        fields = ('title', 'reference', 'description', 'status', 'created_at', 'location', 'resident', 'reports')

class ReportSerializer(serializers.ModelSerializer):
    status  = StatusField(read_only=False)
    staff   = serializers.HyperlinkedRelatedField(many=False, read_only=False, view_name='staff-detail', queryset=Staff.objects.all())
    enquire = serializers.HyperlinkedRelatedField(many=False, read_only=False, view_name='enquire-detail', queryset=Enquire.objects.all())
    
    class Meta:
        model = Report
        fields = ('reference', 'description', 'status', 'created_at', 'enquire', 'staff')