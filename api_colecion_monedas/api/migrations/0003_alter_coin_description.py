# Generated by Django 4.0.2 on 2022-02-11 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_agno_coin_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
    ]