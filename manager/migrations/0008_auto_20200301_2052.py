# Generated by Django 3.0.3 on 2020-03-01 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_auto_20200301_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateandslot',
            name='booking_date',
            field=models.DateField(),
        ),
    ]