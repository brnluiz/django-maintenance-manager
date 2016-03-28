from rest_framework import serializers

from .models import Room
from .models import Flat
from .models import Location

from .models import Role
from .models import Employee

class RoomSerializer(serializers.ModelSerializer):
    flat = serializers.HyperlinkedRelatedField(many=False, view_name='flat-detail', read_only=True)

    class Meta:
        model = Flat
        fields = ('identificator', 'flat')

class FlatSerializer(serializers.ModelSerializer):
    location = serializers.HyperlinkedRelatedField(many=False, view_name='location-detail', read_only=True)
    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = Flat
        fields = ('identificator', 'location', 'rooms')

class LocationSerializer(serializers.ModelSerializer):
    flats = serializers.HyperlinkedRelatedField(many=True, view_name='flat-detail', read_only=True)

    class Meta:
        model = Location
        fields = ('postal', 'city', 'address', 'building', 'flats')

# Employee Serializers

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('title', 'level')

class EmployeeSerializer(serializers.ModelSerializer):
    role = serializers.SlugRelatedField(many=False, read_only=True, slug_field='title')
    class Meta:
        model = Employee
        fields = ('name', 'surname', 'email', 'phone', 'created_at', 'role')