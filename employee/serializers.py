from django.db import models
from rest_framework import serializers

from .models import Position, Employee


class EmployeeSerializer(serializers.ModelSerializer):

    commander = serializers.SerializerMethodField()

    def get_commander(self, obj):
        """
        Рекурсивно берет данные о вышестоящем сотруднике
        """
        return EmployeeSerializer(instance=obj.commander).data

    class Meta:
        model = Employee
        fields = ["id", "full_name", "commander"]

class PositionSerializer(serializers.ModelSerializer):

    employers = EmployeeSerializer(many=True)

    class Meta:
        model = Position
        fields = ["id", "title", "employers"]

