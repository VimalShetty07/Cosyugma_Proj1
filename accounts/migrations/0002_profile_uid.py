# Generated by Django 4.1.1 on 2022-10-07 14:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
