from django.db import models


class Location(models.Model):
    title = models.CharField("Название", max_length=200)
    short_describtion = models.CharField("Краткое описание", max_length=300)
    long_describtion = models.TextField("Полное описание")
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")

    def __str__(self):
        return self.title


class LocationImage(models.Model):
    title = models.CharField("Название", max_length=200)
    image = models.ImageField("Изображение")
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
        verbose_name='Локация',
        related_name='loc_img'
        )
    position = models.SmallIntegerField("Позиция")

    def __str__(self) -> str:
        return f"{self.position} {self.title}"
