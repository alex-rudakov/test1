# Generated by Django 2.1.12 on 2019-09-21 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_auto_20190921_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=15, null=True, verbose_name='Rate'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=15, null=True, verbose_name='Volume'),
        ),
    ]
