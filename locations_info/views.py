from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from locations_info.models import Locations
from locations_info.serializers import LocationSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework.views import APIView


class LocationList(APIView):
    """
    List all Locations, or create a new Location.
    """
    def get(self, request, format=None):
        locations = Locations.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetail(APIView):
    """
    Retrieve, update or delete a Location instance.
    """
    def get_object(self, pk):
        try:
            return Locations.objects.get(pk=pk)
        except Locations.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)