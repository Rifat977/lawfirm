# Generated by Django 5.0.6 on 2024-06-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_service_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]