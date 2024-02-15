from django.db import models
from users.models import User
from datetime import datetime
from django.utils.translation import gettext_lazy

class Packages(models.Model):
    class PackagesObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(start_date__gt=datetime.now())
    
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    days = models.IntegerField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    slots = models.IntegerField()
    creator=models.ForeignKey(User,related_name='package_admin',on_delete=models.PROTECT)

    objects=models.Manager()
    active_packages=PackagesObjects()

    def __str__(self):
        return self.name
    
class Amenities(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    package=models.ForeignKey(Packages,on_delete=models.CASCADE,related_name='amenities')
    
    def __str__(self):
        return self.name


def profile_image_path(instance, filename):
    return f'places/{instance.package.name}/{filename}'

class Places(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    package=models.ForeignKey(Packages,on_delete=models.CASCADE,related_name='places')
    Img=models.ImageField(gettext_lazy("Image"),upload_to=profile_image_path) #default='places/default.jpg')

    def __str__(self):
        return self.name

    
