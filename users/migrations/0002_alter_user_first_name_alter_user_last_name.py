# Generated by Django 4.2.7 on 2024-09-09 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, db_index=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, db_index=True, max_length=150),
        ),
    ]