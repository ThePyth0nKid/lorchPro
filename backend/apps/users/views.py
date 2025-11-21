"""
User Views (API Endpoints)
"""

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import User, APIKey
from .serializers import UserSerializer, UserCreateSerializer, APIKeySerializer


@extend_schema_view(
    list=extend_schema(description='Liste aller Benutzer abrufen'),
    retrieve=extend_schema(description='Einzelnen Benutzer abrufen'),
    create=extend_schema(description='Neuen Benutzer erstellen'),
    update=extend_schema(description='Benutzer aktualisieren'),
    partial_update=extend_schema(description='Benutzer teilweise aktualisieren'),
    destroy=extend_schema(description='Benutzer löschen'),
)
class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet für User-Management
    """
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer
    
    @extend_schema(description='Aktuell eingeloggten Benutzer abrufen')
    @action(detail=False, methods=['get'])
    def me(self, request):
        """Gibt den aktuell authentifizierten User zurück"""
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(description='Eigene API-Keys auflisten'),
    create=extend_schema(description='Neuen API-Key erstellen'),
    destroy=extend_schema(description='API-Key löschen'),
)
class APIKeyViewSet(viewsets.ModelViewSet):
    """
    ViewSet für API-Key-Management
    Nur eigene Keys können verwaltet werden
    """
    serializer_class = APIKeySerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']  # Kein Update von Keys
    
    def get_queryset(self):
        """User sieht nur eigene API-Keys"""
        return APIKey.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """API-Key für aktuellen User erstellen"""
        serializer.save(user=self.request.user)

