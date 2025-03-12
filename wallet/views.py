from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Wallet
from .serializers import WalletSerializer


class WalletViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["created"]
    ordering = ["-created"]
    search_fields = ["id", "label"]
