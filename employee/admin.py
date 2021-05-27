from django.contrib import admin
from .models import Position, Employee


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    """
    Класс для отображение и изменения Модели в Админ панели
    """
    
    def get_queryset(self, request):
        """
        Изменям стандатрный запрос в БД
        """
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('organization').all()
        return queryset

    list_display = ["title", "organization"]



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Класс для отображение и изменения Модели в Админ панели
    """

    list_display = ["last_name", "first_name", "middle_name"]