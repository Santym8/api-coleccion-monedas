# Generated by Django 4.0.2 on 2022-02-14 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_coin_image_alter_collector_coins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='image',
            field=models.URLField(),
        ),
    ]
