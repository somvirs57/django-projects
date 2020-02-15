# Generated by Django 3.0.1 on 2020-02-01 16:56

from django.db import migrations, models
import general.models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_auto_20200130_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image1', models.ImageField(blank=True, upload_to=general.models.get_image_filename, verbose_name='Image1')),
                ('image2', models.ImageField(blank=True, upload_to=general.models.get_image_filename, verbose_name='Image2')),
                ('image3', models.ImageField(blank=True, upload_to=general.models.get_image_filename, verbose_name='Image3')),
                ('image4', models.ImageField(blank=True, upload_to=general.models.get_image_filename, verbose_name='Image4')),
                ('image5', models.ImageField(blank=True, upload_to=general.models.get_image_filename, verbose_name='Image5')),
                ('image6', models.ImageField(blank=True, upload_to=general.models.get_image_filename, verbose_name='Image6')),
                ('image7', models.ImageField(blank=True, upload_to=general.models.get_image_filename, verbose_name='Image7')),
                ('image8', models.ImageField(blank=True, upload_to=general.models.get_image_filename, verbose_name='Image8')),
                ('image9', models.ImageField(blank=True, upload_to=general.models.get_image_filename, verbose_name='Image9')),
                ('image10', models.ImageField(blank=True, upload_to=general.models.get_image_filename, verbose_name='Image10')),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]