# Generated by Django 3.0.1 on 2020-02-12 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slot_book', '0004_auto_20200212_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetails',
            name='slot_date',
            field=models.DateField(),
        ),
    ]