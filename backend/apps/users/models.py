"""
User Models für lorchPro
Custom User Model mit Email-Auth und API-Key Support
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
import secrets


class User(AbstractUser):
    """
    Custom User Model mit UUID Primary Key und Email-basierter Authentifizierung
    """
    class Rolle(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrator'
        AUSSENDIENST = 'AUSSENDIENST', 'Außendienst'
        BUERO = 'BUERO', 'Büro/Sekretariat'
    
    # UUID als Primary Key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Email als Username Field
    email = models.EmailField(unique=True, verbose_name='E-Mail-Adresse')
    
    # Zusätzliche Felder
    rolle = models.CharField(
        max_length=20,
        choices=Rolle.choices,
        default=Rolle.AUSSENDIENST,
        verbose_name='Rolle'
    )
    telefon = models.CharField(max_length=20, blank=True, verbose_name='Telefon')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Aktualisiert am')
    
    # Email als Username verwenden
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    class Meta:
        verbose_name = 'Benutzer'
        verbose_name_plural = 'Benutzer'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_rolle_display()})"


class APIKey(models.Model):
    """
    API-Keys für externe Programm-Integrationen
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='api_keys',
        verbose_name='Benutzer'
    )
    name = models.CharField(max_length=100, verbose_name='Name')
    key = models.CharField(max_length=64, unique=True, verbose_name='API-Key')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am')
    expires_at = models.DateTimeField(null=True, blank=True, verbose_name='Läuft ab am')
    last_used_at = models.DateTimeField(null=True, blank=True, verbose_name='Zuletzt verwendet')
    
    class Meta:
        db_table = 'api_keys'
        verbose_name = 'API-Key'
        verbose_name_plural = 'API-Keys'
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        # API-Key generieren wenn noch nicht vorhanden
        if not self.key:
            self.key = f"lpk_{secrets.token_urlsafe(48)}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} ({self.user.email})"

