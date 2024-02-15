from rest_framework import serializers
from .models import Packages,Amenities,Places

class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Amenities
        fields=['id','name','description']

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Places
        fields=['id','name','description','Img']

#places=PlacesSerializer(many=True)
#amenities=AmenitiesSerializer(many=True)
class PackagesSerializer(serializers.ModelSerializer):
    #places=PlacesSerializer(many=True)
    #amenities=AmenitiesSerializer(many=True)
    class Meta:
        model=Packages
        fields=[
            "id",
            "name",
            "description",
            "days",
            "price",
            "start_date",
            "end_date",
            "slots",

        ]
    #def create()

class BasicDetailPackageSerializer(serializers.ModelSerializer):
    places=serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name')
    
    amenities = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    class Meta:
        model=Packages
        fields=['id','name','description','start_date','end_date','amenities','places']


class CompletePackagesSerializer(serializers.ModelSerializer):
    places=PlacesSerializer(many=True)
    amenities=AmenitiesSerializer(many=True)
    class Meta:
        model=Packages
        fields=[
            "id",
            "name",
            "description",
            "days",
            "price",
            "start_date",
            "end_date",
            "slots",
            "places",
            "amenities"]