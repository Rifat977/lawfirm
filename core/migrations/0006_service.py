# Generated by Django 5.0.6 on 2024-06-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_sitesettings_practice_areas_alter_sitesettings_logo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='services/')),
                ('description', models.TextField()),
            ],
        ),
    ]