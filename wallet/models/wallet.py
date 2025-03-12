import uuid

from django_extensions.db.models import TimeStampedModel
from django.db import models


class Wallet(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField()