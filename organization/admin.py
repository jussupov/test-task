from django.contrib import admin
from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """
    Класс для отображение и изменения Модели в Админ панели
    """
    
    pass