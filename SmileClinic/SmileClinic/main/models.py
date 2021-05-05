from django.db import models
from datetime import date
from django.utils import timezone


class Specialists(models.Model):

    name = models.CharField("Имя", max_length=100)
    secondname = models.CharField("Отчество", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    expirience = models.IntegerField("Опыт работы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"


class Records(models.Model):

    CONFIRMED = "RC"
    CONDUCTED = "SC"
    DISRUPTED = "ED"

    STATUS_CHOICES = [
        (CONFIRMED, "Запись подтверждена"),
        (CONDUCTED, "Обследование проведено"),
        (DISRUPTED, "Обследование сорвано"),
    ]

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default=CONFIRMED,
    )
    date = models.DateField("Дата записи", default=date.today)
    time = models.DateTimeField("Время записи", default=timezone.now)
    doctor = models.ForeignKey(
        Specialists,
        verbose_name="Специалист",
        on_delete=models.SET_NULL,
        null=True
    )
    email = models.EmailField("Email клиента",max_length=254)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
