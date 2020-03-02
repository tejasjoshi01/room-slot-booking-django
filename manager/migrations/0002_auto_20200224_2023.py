# Generated by Django 3.0.3 on 2020-02-24 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateandslot',
            name='booking_slot',
            field=models.TextField(choices=[('22:00:00', 'S1'), ('10:00:00', 'S2')]),
        ),
        migrations.CreateModel(
            name='AvailableRooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms_available', models.IntegerField(default=False)),
                ('booking_date_slot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manager.DateAndSlot')),
            ],
        ),
    ]