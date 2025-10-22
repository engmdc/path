from django.contrib import admin
from .models import EventType, Facility, Hall

# Enhanced EventType Admin with permissions
@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    
    # Permissions handling
    def has_add_permission(self, request):
        # Check if user has permission to add an event type
        return request.user.has_perm('hall.add_eventtype')
    
    def has_change_permission(self, request, obj=None):
        # Check if user has permission to change an event type
        return request.user.has_perm('hall.change_eventtype')
    
    def has_delete_permission(self, request, obj=None):
        # Check if user has permission to delete an event type
        return request.user.has_perm('hall.delete_eventtype')
    
    def has_view_permission(self, request, obj=None):
        # Check if user has permission to view an event type
        return request.user.has_perm('hall.view_eventtype')

# Enhanced Facility Admin with permissions
@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'additional_price', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    
    # Permissions handling
    def has_add_permission(self, request):
        # Check if user has permission to add a facility
        return request.user.has_perm('hall.add_facility')
    
    def has_change_permission(self, request, obj=None):
        # Check if user has permission to change a facility
        return request.user.has_perm('hall.change_facility')
    
    def has_delete_permission(self, request, obj=None):
        # Check if user has permission to delete a facility
        return request.user.has_perm('hall.delete_facility')
    
    def has_view_permission(self, request, obj=None):
        # Check if user has permission to view a facility
        return request.user.has_perm('hall.view_facility')

# Enhanced Hall Admin with permissions
@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'location', 'capacity', 'price_per_guest', 'is_available')
    list_filter = ('is_available', 'created_at')
    search_fields = ('name', 'location', 'company')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('company', 'name', 'location', 'capacity', 'is_available')
        }),
        ('Financial Details', {
            'fields': ('price_per_guest', 'income_account', 'extra_income_account', 'receivable_account')
        }),
        ('Additional Information', {
            'fields': ('facilities', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    # Permissions handling
    def has_add_permission(self, request):
        # Check if user has permission to add a hall
        return request.user.has_perm('hall.add_hall')
    
    def has_change_permission(self, request, obj=None):
        # Check if user has permission to change a hall
        return request.user.has_perm('hall.change_hall')
    
    def has_delete_permission(self, request, obj=None):
        # Check if user has permission to delete a hall
        return request.user.has_perm('hall.delete_hall')
    
    def has_view_permission(self, request, obj=None):
        # Check if user has permission to view a hall
        return request.user.has_perm('hall.view_hall')
