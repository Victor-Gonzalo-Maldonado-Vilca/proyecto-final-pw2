# Generated by Django 5.0.7 on 2024-07-21 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CyberManage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='price_per_hour',
        ),
    ]