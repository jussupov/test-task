import uuid
from decimal import Decimal

from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel

from transactions.fields import TxIDField


class Transactions(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wallet = models.ForeignKey(
        to="wallet.Wallet", on_delete=models.PROTECT, related_name="transactions"
    )
    txid = TxIDField()
    amount = models.DecimalField(
        max_digits=36, decimal_places=18, validators=[MinValueValidator(Decimal("0"))]
    )

    def clean(self):
        # validate that the transaction amount is greater than zero
        if self.amount <= 0:
            raise ValidationError("Transaction amount must be greater than zero.")

    def save(self, *args, **kwargs):
        # validate the transaction before saving
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        indexes = [models.Index(fields=["txid"], name="txid_idx")]


@receiver(post_save, sender=Transactions)
@receiver(post_delete, sender=Transactions)
def clear_wallet_balance_cache(sender, instance, **kwargs):
    # clear cache when a transaction is created or deleted
    cache_key = f"wallet_balance_{instance.wallet.id}"
    cache.delete(cache_key)
