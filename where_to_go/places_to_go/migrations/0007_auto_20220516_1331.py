# Generated by Django 3.1.14 on 2022-05-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_to_go', '0006_alter_locationimage_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locationimage',
            options={'ordering': ['position']},
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='locationimage',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='locationimage',
            name='position',
            field=models.PositiveIntegerField(default=0, verbose_name='Позиция'),
        ),
    ]
