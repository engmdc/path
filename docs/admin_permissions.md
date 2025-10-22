# Django Admin Permissions Guide

This document outlines how to use and manage permissions in the Django admin interface for the Path application.

## Overview

The Path application uses Django's built-in permissions system and Jazzmin for an enhanced admin interface. Permissions are assigned to users either directly or through groups.

## Permission Groups

Three default permission groups have been set up:

1. **Administrators**: Full access to all models and functions
2. **Managers**: Can view and edit data but cannot add or delete records
3. **Staff**: View-only access to all data

## Setting Up Permissions

To initialize the default permission groups, run:

```bash
python manage.py setup_permissions
```

This command creates the default groups and assigns appropriate permissions to each group.

## Assigning Permissions to Users

1. Log in to the admin interface (`/admin/`)
2. Navigate to "Authentication and Authorization" > "Users"
3. Select a user to edit
4. In the "Permissions" section:
   - Assign user to appropriate groups
   - OR assign individual permissions

## Permission Types

Django provides four types of permissions for each model:

1. **add**: Ability to add new records
2. **change**: Ability to modify existing records
3. **delete**: Ability to remove records
4. **view**: Ability to view records

## Hall App Permissions

The Hall app contains three models, each with its own set of permissions:

### Hall Model
- `hall.add_hall`: Create new halls
- `hall.change_hall`: Edit existing halls
- `hall.delete_hall`: Remove halls
- `hall.view_hall`: View halls

### EventType Model
- `hall.add_eventtype`: Create new event types
- `hall.change_eventtype`: Edit existing event types
- `hall.delete_eventtype`: Remove event types
- `hall.view_eventtype`: View event types

### Facility Model
- `hall.add_facility`: Create new facilities
- `hall.change_facility`: Edit existing facilities
- `hall.delete_facility`: Remove facilities
- `hall.view_facility`: View facilities

## Best Practices

1. **Use Groups**: Assign permissions to groups rather than individual users for easier management
2. **Principle of Least Privilege**: Give users only the permissions they need
3. **Regular Audits**: Periodically review user permissions
4. **Test Permissions**: After setting up permissions, test them with different users

## Troubleshooting

If a user cannot access certain features:

1. Check if the user is assigned to the correct group
2. Verify individual permissions assigned to the user
3. Ensure the user has both the model permission and any related view permissions
4. Check if the user is marked as "staff" (required for admin access)

## Additional Configuration

For advanced permission configuration, you can modify:

- `dashboard/admin.py`: Custom admin classes for auth models
- `hall/admin.py`: Permission handling for hall-related models
- `project/jazzmin_settings.py`: Admin interface customization
