# Generated by Django 2.0 on 2019-07-23 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20190723_1443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deal',
            options={'ordering': ['-deal_date']},
        ),
    ]
