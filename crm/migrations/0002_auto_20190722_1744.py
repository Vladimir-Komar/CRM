# Generated by Django 2.0 on 2019-07-22 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Add Photo to Customer'),
        ),
    ]
