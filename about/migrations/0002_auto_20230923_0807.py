# Generated by Django 3.2.21 on 2023-09-23 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Info Categories',
            },
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name_plural': 'FAQs'},
        ),
        migrations.AlterModelOptions(
            name='testimonial',
            options={'verbose_name_plural': 'Testimonials'},
        ),
    ]
