from django.shortcuts import render
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import OrganizationSerializer
from .models import Organization

class OrganizationViewSet(RetrieveModelMixin, GenericViewSet):
    serializer_class = OrganizationSerializer
    queryset = (Organization
                    .objects
                    .prefetch_related('positions')
                    .all()
    )