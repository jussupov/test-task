import hashlib
import uuid
from decimal import Decimal

import pytest
from django.core.cache import cache
from django.core.exceptions import ValidationError
from rest_framework.test import APIClient

from transactions.models import Transactions
from wallet.models import Wallet  # Импортируем модель кошелька


@pytest.fixture
def wallet(db):
    return Wallet.objects.create(id=uuid.uuid4())


@pytest.mark.django_db
def test_transaction_creation(wallet):
    txid = hashlib.sha256(uuid.uuid4().bytes).hexdigest()
    transaction = Transactions.objects.create(
        wallet=wallet, txid=txid, amount=Decimal("10.0")
    )
    assert transaction.id is not None
    assert transaction.wallet == wallet
    assert transaction.amount == Decimal("10.0")


@pytest.mark.django_db
def test_transaction_amount_validation(wallet):
    with pytest.raises(
        ValidationError, match="Transaction amount must be greater than zero"
    ):
        txid = hashlib.sha256(uuid.uuid4().bytes).hexdigest()
        transaction = Transactions(wallet=wallet, txid=txid, amount=Decimal("-5.0"))
        transaction.full_clean()


@pytest.mark.django_db
def test_cache_clear_on_transaction_creation(wallet):
    cache_key = f"wallet_balance_{wallet.id}"
    cache.set(cache_key, "cached_value")
    txid = hashlib.sha256(uuid.uuid4().bytes).hexdigest()
    Transactions.objects.create(wallet=wallet, txid=txid, amount=Decimal("10.0"))
    assert cache.get(cache_key) is None


@pytest.mark.django_db
def test_cache_clear_on_transaction_deletion(wallet):
    cache_key = f"wallet_balance_{wallet.id}"
    txid = hashlib.sha256(uuid.uuid4().bytes).hexdigest()
    transaction = Transactions.objects.create(
        wallet=wallet, txid=txid, amount=Decimal("10.0")
    )
    cache.set(cache_key, "cached_value")
    transaction.delete()
    assert cache.get(cache_key) is None


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_transactions_api_list(api_client, wallet):
    txid = hashlib.sha256(uuid.uuid4().bytes).hexdigest()
    Transactions.objects.create(wallet=wallet, txid=txid, amount=Decimal("10.0"))
    response = api_client.get("/api/v1/transactions/")
    assert response.status_code == 200
    assert len(response.json()) > 0
