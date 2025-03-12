import django_filters

from .models import Transactions


class TransactionsFilter(django_filters.FilterSet):
    amount_min = django_filters.NumberFilter(
        field_name="amount", lookup_expr="gte"
    )  # Минимальная сумма
    amount_max = django_filters.NumberFilter(
        field_name="amount", lookup_expr="lte"
    )  # Максимальная сумма
    created_after = django_filters.DateTimeFilter(
        field_name="created", lookup_expr="gte"
    )  # Дата от
    created_before = django_filters.DateTimeFilter(
        field_name="created", lookup_expr="lte"
    )  # Дата до

    class Meta:
        model = Transactions
        fields = [
            "wallet",
            "txid",
            "amount_min",
            "amount_max",
            "created_after",
            "created_before",
        ]
