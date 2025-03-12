import uuid
from decimal import Decimal

from django.db import models

from django_extensions.db.models import TimeStampedModel

from transactions.fields import TxIDField
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class Transactions(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wallet = models.ForeignKey(to='wallet.Wallet', on_delete=models.PROTECT, related_name='transactions')
    txid = TxIDField()
    amount = models.DecimalField(
        max_digits=36,
        decimal_places=18,  
        validators=[MinValueValidator(Decimal('0'))] 
    )

    def clean(self):
        if self.amount <= 0:
            raise ValidationError("Transaction amount must be greater than zero.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=['txid'], name='txid_idx')
        ]