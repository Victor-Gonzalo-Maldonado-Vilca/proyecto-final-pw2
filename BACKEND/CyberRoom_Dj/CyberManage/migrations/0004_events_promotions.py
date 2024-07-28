# Generated by Django 5.0.7 on 2024-07-21 21:56

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CyberManage', '0003_remove_reservation_idproduct_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nameEvent', models.CharField(max_length=17)),
                ('description', models.TextField()),
                ('startDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('completionDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('namePromotion', models.CharField(max_length=17)),
                ('description', models.TextField(max_length=500)),
                ('startDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('completionDate', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CyberManage.events')),
            ],
        ),
    ]