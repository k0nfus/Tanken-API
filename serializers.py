from rest_framework import serializers
from .models import Tanken

class TankenListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanken
        fields = [
            "id",
            "datum",
            "betrag",
            "bemerkung",
        ]

class TankenDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanken
        fields = [
            "id",
            "datum",
            "betrag",
            "bemerkung",
        ]