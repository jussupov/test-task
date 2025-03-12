from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .filters import TransactionsFilter  # Импортируем фильтр
from .models import Transactions
from .serializers import TransactionsSerializer


class TransactionsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = TransactionsFilter  # Указываем кастомный фильтр
    ordering_fields = ["amount", "created"]
    ordering = ["-created"]
    search_fields = ["id", "txid"]
