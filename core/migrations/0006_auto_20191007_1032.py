# Generated by Django 2.2.6 on 2019-10-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_saldo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saldo',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
