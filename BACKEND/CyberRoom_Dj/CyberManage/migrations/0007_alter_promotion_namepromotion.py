# Generated by Django 5.0.7 on 2024-07-22 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CyberManage', '0006_remove_promotion_event_alter_event_nameevent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='namePromotion',
            field=models.CharField(max_length=50),
        ),
    ]
