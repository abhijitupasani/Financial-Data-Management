from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Account, Transaction, AuditLog

def log_audit(instance, action, changed_by=None, changes=""):
    AuditLog.objects.create(
        model_name=instance.__class__.__name__,
        object_id=instance.pk,
        action=action,
        changed_by=changed_by,
        changes=changes
    )

@receiver(post_save, sender=Account)
def account_post_save(sender, instance, created, **kwargs):
    user = getattr(instance, '_changed_by', None)
    if not user:
        return
    action = 'CREATE' if created else 'UPDATE'
    log_audit(instance, action, changed_by=user, changes=f"{action} performed")

@receiver(post_delete, sender=Account)
def account_post_delete(sender, instance, **kwargs):
    user = getattr(instance, '_changed_by', None)
    if not user:
        return
    log_audit(instance, 'DELETE', changed_by=user, changes="Deleted account")

@receiver(post_save, sender=Transaction)
def transaction_post_save(sender, instance, created, **kwargs):
    user = getattr(instance, '_changed_by', None)
    if not user:
        return
    action = 'CREATE' if created else 'UPDATE'
    log_audit(instance, action, changed_by=user, changes=f"{action} performed")

@receiver(post_delete, sender=Transaction)
def transaction_post_delete(sender, instance, **kwargs):
    user = getattr(instance, '_changed_by', None)
    if not user:
        return
    log_audit(instance, 'DELETE', changed_by=user, changes="Deleted transaction")
