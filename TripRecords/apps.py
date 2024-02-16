from django.apps import AppConfig


class TriprecordsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "TripRecords"

    def ready(self):
        import TripRecords.signals
