# Generated by Django 2.1.15 on 2020-05-05 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LifePlanner', '0005_journal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Assigned'),
        ),
    ]
