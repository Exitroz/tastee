# Generated by Django 4.0.4 on 2022-08-26 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_food_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='quantity',
        ),
    ]
