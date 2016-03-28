from rest_framework import serializers

from .models import Location
from .models import Flat
from .models import Room

class LocationSerializer(serializers.ModelSerializer):
    flats = serializers.HyperlinkedRelatedField(many=True, view_name='flat-detail', read_only=True)

    class Meta:
        model = Location
        fields = ('postal', 'city', 'address', 'building', 'flats')

class FlatSerializer(serializers.ModelSerializer):
    location = serializers.HyperlinkedRelatedField(many=False, view_name='location-detail', read_only=True)
    rooms = serializers.HyperlinkedRelatedField(many=True, view_name='room-detail', read_only=True)

    class Meta:
        model = Flat
        fields = ('identificator', 'location', 'rooms')

class RoomSerializer(serializers.ModelSerializer):
    flat = serializers.HyperlinkedRelatedField(many=False, view_name='flat-detail', read_only=True)

    class Meta:
        model = Flat
        fields = ('identificator', 'flat')