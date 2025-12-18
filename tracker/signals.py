from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Application, ApplicationStatusHistory

@receiver(pre_save, sender=Application)
def log_status_change(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        previous = Application.objects.get(pk=instance.pk)
    except Application.DoesNotExist:
        return
    if previous.status != instance.status:
        ApplicationStatusHistory.objects.create(
            application=instance,
            old_status=previous.status,
            new_status=instance.status,
        )
