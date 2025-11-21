"""
User Admin
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, APIKey


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Admin für Custom User Model"""
    
    list_display = ['email', 'username', 'first_name', 'last_name', 'rolle', 'is_active', 'is_staff']
    list_filter = ['rolle', 'is_active', 'is_staff', 'created_at']
    search_fields = ['email', 'username', 'first_name', 'last_name']
    ordering = ['-created_at']
    
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Persönliche Informationen', {'fields': ('first_name', 'last_name', 'telefon')}),
        ('Rolle & Berechtigungen', {'fields': ('rolle', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Zeitstempel', {'fields': ('last_login', 'date_joined', 'created_at', 'updated_at')}),
    )
    
    readonly_fields = ['created_at', 'updated_at', 'last_login', 'date_joined']
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'rolle'),
        }),
    )


@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    """Admin für API-Keys"""
    
    list_display = ['name', 'user', 'key_preview', 'created_at', 'expires_at', 'last_used_at']
    list_filter = ['created_at', 'expires_at']
    search_fields = ['name', 'user__email', 'key']
    readonly_fields = ['key', 'created_at', 'last_used_at']
    
    def key_preview(self, obj):
        """Zeige nur Anfang des Keys"""
        return f"{obj.key[:20]}..."
    key_preview.short_description = 'API-Key'

