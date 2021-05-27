from django.db import models
from django.db.models.base import Model

class Position(models.Model):
    """
    Модель Должности
    """
    title = models.CharField(max_length=255, verbose_name="Название должности")
    organization = models.ForeignKey(to="organization.Organization", on_delete=models.CASCADE, related_name="positions")
    

    def __str__(self) -> str:
        """
        Возвращает имя объекта
        """
        return "%s / %s" % (self.organization, self.title)


class Employee(models.Model):
    """
    Модель Работника
    """
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    middle_name = models.CharField(max_length=255, verbose_name="Отчество", blank=True, null=True)
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")

    position = models.ManyToManyField(to="Position", related_name="employers")
    commander = models.ForeignKey(to="self", on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def full_name(self):
        """
        Возвращает полное имя работника
        """
        return "%s %s %s" % (self.last_name, self.first_name, self.middle_name)

    def __str__(self) -> str:
        return self.full_name