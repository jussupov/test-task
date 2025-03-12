import hashlib
import uuid
from decimal import Decimal

import pytest
from django.core.cache import cache
from rest_framework.test import APIClient

from transactions.models import Transactions
from wallet.models import Wallet


@pytest.fixture
def wallet(db):
    return Wallet.objects.create(id=uuid.uuid4(), label="Test Wallet")


@pytest.mark.django_db
def test_wallet_balance_cache(wallet):
    cache_key = f"wallet_balance_{wallet.id}"
    cache.set(cache_key, Decimal("20.0"))
    assert wallet.balance == Decimal("20.0")


@pytest.mark.django_db
def test_wallet_balance(wallet):
    assert wallet.balance == 0
    txid1 = hashlib.sha256(uuid.uuid4().bytes).hexdigest()
    txid2 = hashlib.sha256(uuid.uuid4().bytes).hexdigest()
    Transactions.objects.create(wallet=wallet, txid=txid1, amount=Decimal("10.0"))
    Transactions.objects.create(wallet=wallet, txid=txid2, amount=Decimal("5.0"))
    assert wallet.balance == Decimal("15.0")


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_wallet_api_list(api_client, wallet):
    response = api_client.get("/api/v1/wallets/")
    assert response.status_code == 200
    assert len(response.json()) > 0
