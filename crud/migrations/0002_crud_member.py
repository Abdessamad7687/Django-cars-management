# Generated by Django 4.1.5 on 2023-05-09 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='crud_Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('mobile_number', models.CharField(blank=True, max_length=10)),
                ('description', models.TextField(max_length=255)),
                ('location', models.TextField(max_length=255)),
                ('date', models.DateField(verbose_name='%m/%d/%Y')),
                ('created_at', models.DateTimeField(verbose_name='%m/%d/%Y %H:%M:%S')),
                ('updated_at', models.DateTimeField(verbose_name='%m/%d/%Y %H:%M:%S')),
            ],
        ),
    ]