# Generated by Django 4.2.2 on 2025-06-22 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='email',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='name',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.telegramuser'),
        ),
    ]
