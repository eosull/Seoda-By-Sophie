# Generated by Django 3.2.21 on 2023-09-26 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options_product_on_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='out_of_stock',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
