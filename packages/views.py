from rest_framework import generics, viewsets, filters
from .models import Packages,Amenities,Places
from .serializers import PackagesSerializer,AmenitiesSerializer,PlacesSerializer,BasicDetailPackageSerializer,CompletePackagesSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated, IsAuthenticatedOrReadOnly,AllowAny
from .permissions import ReadOnly,IsAdminOrReadOnly,IsAdmin_Obj
from django.http import Http404
from datetime import datetime 
from rest_framework.exceptions import PermissionDenied



class PackagesListCreate(generics.ListCreateAPIView):
    """user read only Admin to read and write"""
    permission_classes = [IsAdminUser|IsAuthenticated]
    queryset=Packages.active_packages.all()
    serializer_class=PackagesSerializer
    filter_backends=[filters.OrderingFilter,filters.SearchFilter]
    search_fields= ['^name','^description']
    ordering_fields=['start_date','end_date','name']
    ordering=['id']
    
    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            serializer.save(creator=self.request.user)
        else:
            raise PermissionDenied("You are not authorized to perform this action. Only admin users can create packages.")

class CompletePackageDetail(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Packages.objects.all()
    serializer_class =CompletePackagesSerializer
    #lookup_kwargs=['id']

class PackagesDetail(generics.RetrieveUpdateDestroyAPIView):#PackageRetrieveUpdateDestroyAPIView
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Packages.objects.all()
    serializer_class =PackagesSerializer


class OldPackages(generics.ListAPIView):
    permission_classes=[IsAdminUser|ReadOnly]
    queryset = Packages.objects.filter(start_date__gt=datetime.now())
    serializer_class = PackagesSerializer


class AmenitiesList(generics.ListCreateAPIView):
    permission_classes=[IsAdminUser|ReadOnly]
    #queryset=Amenities.objects.all()
    serializer_class=AmenitiesSerializer

    def get_queryset(self):
        package_id = self.kwargs['package']
        package = Packages.objects.filter(id=package_id).first()
        return Amenities.objects.filter(package=package)
    
    def perform_create(self, serializer):
        package_id = self.kwargs['package']
        package = Packages.objects.filter(id=package_id).first()
        serializer.save(package=package)


class AmenityDetail(generics.RetrieveUpdateDestroyAPIView):
    #API endpoint to manage amenities for a certain package.
    permission_classes=[IsAdminUser|ReadOnly]
    queryset = Amenities.objects.all()
    serializer_class = AmenitiesSerializer
    lookup_url_kwarg = 'amenity_id'

    def get_queryset(self):
        #print(self.request.data,self.args,self.kwargs)
        package_id = self.kwargs['package']
        return Amenities.objects.filter(package=package_id)


class PlacesList(generics.ListCreateAPIView):
    permission_classes=[IsAdminOrReadOnly]
    queryset=Places.objects.all()
    serializer_class=PlacesSerializer

    def get_queryset(self):
        package_id = self.kwargs['package']
        package = Packages.objects.filter(id=package_id).first()
        return Places.objects.filter(package=package)
    
    def perform_create(self, serializer):
        package_id = self.kwargs['package']
        package = Packages.objects.filter(id=package_id).first()
        serializer.save(package=package)


class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint to manage places for a certain package."""
    permission_classes=[AllowAny]
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer
    lookup_url_kwarg = 'place_id'

    def get_queryset(self):
        id = self.kwargs['package']
        return Places.objects.filter(package=id)