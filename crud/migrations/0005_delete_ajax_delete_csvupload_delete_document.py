# Generated by Django 4.1.5 on 2023-05-10 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_cartbl_delete_car'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ajax',
        ),
        migrations.DeleteModel(
            name='CsvUpload',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
