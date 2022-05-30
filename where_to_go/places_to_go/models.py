from django.db import models
from tinymce.models import HTMLField


class Location(models.Model):
    title = models.CharField("Название", max_length=200, unique=True)
    short_describtion = models.CharField("Краткое описание", max_length=300)
    long_describtion = HTMLField()
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")

    def __str__(self):
        return self.title


class LocationImage(models.Model):
    title = models.CharField("Название", max_length=200, unique=True)
    image = models.ImageField("Изображение")
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
        verbose_name='Локация',
        related_name='images'
        )
    position = models.PositiveIntegerField(
        "Позиция",
        default=0,
        blank=False,
        null=False
        )

    class Meta:
        ordering = ['position', ]

    def __str__(self) -> str:
        return f"{self.position} {self.title}"
