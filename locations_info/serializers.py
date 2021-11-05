from rest_framework import serializers
from locations_info.models import Locations 

class LocationSerializer(serializers.Serializer):
    
    location_code = serializers.CharField(required=True, max_length=5)
    description = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=5)
    

    def create(self, validated_data):
        """
        Create and return a new `Location` instance, given the validated data.
        """
        return Locations.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Location` instance, given the validated data.
        """
        instance.location_code= validated_data.get('location_code', instance.location_code)
        instance.description = validated_data.get('description', instance.description)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance