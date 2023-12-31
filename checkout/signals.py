# Signals to update order when items added

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, *args, **kwargs):
    # Update order total when lineitem created/updated
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, *args, **kwargs):
    # Update order total when lineitem deleted
    instance.order.update_total()
