from rest_framework import serializers
from .models import Organization

from employee.serializers import PositionSerializer

class OrganizationSerializer(serializers.ModelSerializer):

    positions = PositionSerializer(many=True)

    class Meta:
        model = Organization
        fields = ["id", "title", "positions"]


