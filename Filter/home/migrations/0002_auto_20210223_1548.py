# Generated by Django 3.1.6 on 2021-02-23 13:48

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('ADDRESS_TYPE_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('NAME', models.CharField(blank=True, max_length=50, null=True)),
                ('NAME_EN', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'employees',
            },
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
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='رقم السجل'),
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
    ]
