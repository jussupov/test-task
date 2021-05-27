from django.db import models


class Organization(models.Model):
    """
    Модель Организаций
    """
    title = models.CharField(max_length=255, verbose_name="Название организаций")

    def __str__(self) -> str:
        """
        Возвращает имя объекта
        """
        return self.title

