from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import OrganizationViewSet

router = SimpleRouter()

router.register('organization', OrganizationViewSet, basename='organization')

urlpatterns = router.urls
