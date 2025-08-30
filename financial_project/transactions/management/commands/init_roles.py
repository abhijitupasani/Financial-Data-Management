from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from transactions.models import Account, Transaction

class Command(BaseCommand):
    help = 'Create initial user roles and permissions'

    def handle(self, *args, **kwargs):
        # Define roles and permissions
        roles_permissions = {
            'Admin': Permission.objects.all(),
            'Financial Analyst': Permission.objects.filter(
                content_type__model__in=['account', 'transaction'],
                codename__in=['view_account', 'change_account', 'view_transaction', 'change_transaction']
            ),
            'Auditor': Permission.objects.filter(
                content_type__model__in=['account', 'transaction'],
                codename__in=['view_account', 'view_transaction']
            ),
        }

        for role_name, perms in roles_permissions.items():
            role, created = Group.objects.get_or_create(name=role_name)
            role.permissions.set(perms)
            role.save()
            self.stdout.write(self.style.SUCCESS(f'Role {role_name} initialized.'))
