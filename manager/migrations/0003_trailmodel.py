# Generated by Django 2.1.11 on 2020-02-24 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20200224_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='trailmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('re', models.TextField()),
            ],
        ),
    ]
