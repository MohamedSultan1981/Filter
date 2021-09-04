# Generated by Django 3.1.6 on 2021-02-27 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_factory_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='factory',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, through='home.Fact_product', to='home.products', verbose_name='المنتجات'),
        ),
    ]