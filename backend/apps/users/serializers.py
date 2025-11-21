"""
User Serializers
"""

from rest_framework import serializers
from .models import User, APIKey


class UserSerializer(serializers.ModelSerializer):
    """Serializer für User-Objekte"""
    
    class Meta:
        model = User
        fields = [
            'id', 'email', 'username', 'first_name', 'last_name',
            'rolle', 'telefon', 'is_active', 'is_staff',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer für User-Erstellung mit Passwort"""
    
    password = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = [
            'email', 'username', 'first_name', 'last_name',
            'password', 'password_confirm', 'rolle', 'telefon'
        ]
    
    def validate(self, attrs):
        """Passwörter müssen übereinstimmen"""
        if attrs.get('password') != attrs.pop('password_confirm', None):
            raise serializers.ValidationError({'password_confirm': 'Passwörter stimmen nicht überein'})
        return attrs
    
    def create(self, validated_data):
        """User mit gehashtem Passwort erstellen"""
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user


class APIKeySerializer(serializers.ModelSerializer):
    """Serializer für API-Keys"""
    
    class Meta:
        model = APIKey
        fields = ['id', 'name', 'key', 'created_at', 'expires_at', 'last_used_at']
        read_only_fields = ['id', 'key', 'created_at', 'last_used_at']
    
    def create(self, validated_data):
        """API-Key mit aktuellem User erstellen"""
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

