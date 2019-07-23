# Generated by Django 2.0 on 2019-07-19 10:44

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('address', models.CharField(max_length=128)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('customer_image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Add Photo to Article')),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_date', models.DateField()),
                ('deal_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('profit', models.DecimalField(decimal_places=2, max_digits=6)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deal', to='crm.Customer', verbose_name='Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('content', ckeditor.fields.RichTextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Add Photo to product')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('article_image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Add logo')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='crm.Provider', verbose_name='Provider'),
        ),
        migrations.AddField(
            model_name='deal',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deal', to='crm.Product', verbose_name='Product'),
        ),
    ]
