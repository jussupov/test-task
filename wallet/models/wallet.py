import uuid

from django.core.cache import cache
from django.db import models
from django.db.models import Sum
from django_extensions.db.models import TimeStampedModel


class Wallet(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField()

    @property
    def balance(self):
        # decied to add cache to reduce the number of queries
        cache_key = f"wallet_balance_{self.id}"
        balance = cache.get(cache_key)

        if balance is None:
            balance = self.transactions.aggregate(Sum("amount"))["amount__sum"] or 0
            cache.set(cache_key, balance, timeout=300)

        return balance
