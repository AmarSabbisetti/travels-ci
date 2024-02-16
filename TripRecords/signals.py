from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User_Packages

@receiver(post_save, sender=User_Packages)
def update_package_slots(sender, instance, created, **kwargs):
    if created:
        # Get the associated package
        package = instance.package
        
        # Update the slots in the package
        package.slots -= instance.no_of_persons
        package.save()
