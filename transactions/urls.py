from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TransactionsViewSet

router = DefaultRouter()
router.register(r"", TransactionsViewSet, basename="transactions")

urlpatterns = [
    path("", include(router.urls)),
]
