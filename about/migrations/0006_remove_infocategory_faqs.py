# Generated by Django 3.2.21 on 2023-09-23 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_infocategory_faqs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infocategory',
            name='faqs',
        ),
    ]
