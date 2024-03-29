# Generated by Django 3.1.6 on 2021-02-26 18:40

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Productname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='factory',
            name='Factory_Activity',
            field=models.CharField(max_length=100, verbose_name='النشاط'),
        ),
        migrations.AlterField(
            model_name='factory',
            name='Factory_Address',
            field=models.TextField(max_length=500, verbose_name='العنوان'),
        ),
        migrations.AlterField(
            model_name='factory',
            name='Factory_ID',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='رقم المصنع'),
        ),
        migrations.AlterField(
            model_name='factory',
            name='Factory_Manger',
            field=models.CharField(max_length=100, verbose_name='المدير'),
        ),
        migrations.AlterField(
            model_name='factory',
            name='Factory_Name',
            field=models.CharField(max_length=500, verbose_name='اسم المنشأه'),
        ),
        migrations.AlterField(
            model_name='factory',
            name='Factory_city',
            field=models.CharField(max_length=50, verbose_name='المدينة'),
        ),
        migrations.AlterField(
            model_name='factory',
            name='Factory_gov',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.gov', verbose_name='المحافظة'),
        ),
        migrations.AlterField(
            model_name='factory',
            name='Mobile_number',
            field=models.CharField(max_length=12, verbose_name='رقم الموبايل'),
        ),
        migrations.AlterField(
            model_name='factory',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, null=True, region=None, verbose_name='رقم التليفون'),
        ),
        migrations.CreateModel(
            name='registry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registry', models.CharField(max_length=50, unique=True)),
                ('registry_number', models.CharField(max_length=50)),
                ('Factory_ID', models.ForeignKey(db_column='Factory_ID', on_delete=django.db.models.deletion.CASCADE, related_name='my', to='home.factory')),
            ],
        ),
        migrations.CreateModel(
            name='Fact_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Productq', models.CharField(max_length=50)),
                ('Factory_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.factory')),
                ('product_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='t', to='home.products')),
                ('units_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ty', to='home.unit')),
            ],
            options={
                'ordering': ['product_ID'],
            },
        ),
        migrations.AddField(
            model_name='factory',
            name='products',
            field=models.ManyToManyField(through='home.Fact_product', to='home.products', verbose_name='المنتجات'),
        ),
    ]
