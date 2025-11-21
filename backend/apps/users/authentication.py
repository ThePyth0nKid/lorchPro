"""
API-Key Authentication für externe Programme
"""

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.utils import timezone
from .models import APIKey


class APIKeyAuthentication(BaseAuthentication):
    """
    Custom Authentication für API-Keys
    Clients senden: X-API-Key: lpk_xxxxx
    """
    
    def authenticate(self, request):
        api_key = request.headers.get('X-API-Key')
        
        if not api_key:
            return None
        
        try:
            key_obj = APIKey.objects.select_related('user').get(key=api_key)
            
            # Check ob Key abgelaufen ist
            if key_obj.expires_at and key_obj.expires_at < timezone.now():
                raise exceptions.AuthenticationFailed('API-Key ist abgelaufen')
            
            # Letztes Verwendungsdatum aktualisieren
            key_obj.last_used_at = timezone.now()
            key_obj.save(update_fields=['last_used_at'])
            
            return (key_obj.user, key_obj)
            
        except APIKey.DoesNotExist:
            raise exceptions.AuthenticationFailed('Ungültiger API-Key')

