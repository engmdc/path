from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from hall.models import Hall, EventType, Facility

class Command(BaseCommand):
    help = 'Create default permission groups for users'

    def handle(self, *args, **options):
        # Create groups if they don't exist
        admin_group, created = Group.objects.get_or_create(name='Administrators')
        manager_group, created = Group.objects.get_or_create(name='Managers')
        staff_group, created = Group.objects.get_or_create(name='Staff')
        
        # Define content types for our models
        hall_ct = ContentType.objects.get_for_model(Hall)
        eventtype_ct = ContentType.objects.get_for_model(EventType)
        facility_ct = ContentType.objects.get_for_model(Facility)
        
        # Get all permissions for our models
        hall_permissions = Permission.objects.filter(content_type=hall_ct)
        eventtype_permissions = Permission.objects.filter(content_type=eventtype_ct)
        facility_permissions = Permission.objects.filter(content_type=facility_ct)
        
        # Admin group - Full permissions
        admin_group.permissions.add(*hall_permissions)
        admin_group.permissions.add(*eventtype_permissions)
        admin_group.permissions.add(*facility_permissions)
        
        # Manager group - View and change permissions
        manager_permissions = []
        for perm in hall_permissions:
            if 'view' in perm.codename or 'change' in perm.codename:
                manager_permissions.append(perm)
                
        for perm in eventtype_permissions:
            if 'view' in perm.codename or 'change' in perm.codename:
                manager_permissions.append(perm)
                
        for perm in facility_permissions:
            if 'view' in perm.codename or 'change' in perm.codename:
                manager_permissions.append(perm)
                
        manager_group.permissions.add(*manager_permissions)
        
        # Staff group - View-only permissions
        staff_permissions = []
        for perm in hall_permissions:
            if 'view' in perm.codename:
                staff_permissions.append(perm)
                
        for perm in eventtype_permissions:
            if 'view' in perm.codename:
                staff_permissions.append(perm)
                
        for perm in facility_permissions:
            if 'view' in perm.codename:
                staff_permissions.append(perm)
                
        staff_group.permissions.add(*staff_permissions)
        
        # Output results
        self.stdout.write(self.style.SUCCESS(f'Administrators group created with {admin_group.permissions.count()} permissions'))
        self.stdout.write(self.style.SUCCESS(f'Managers group created with {manager_group.permissions.count()} permissions'))
        self.stdout.write(self.style.SUCCESS(f'Staff group created with {staff_group.permissions.count()} permissions'))
