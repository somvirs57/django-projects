# Generated by Django 3.0.1 on 2020-01-28 07:48

from django.db import migrations, models
import django.db.models.deletion
import general.models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=general.models.get_image_filename, verbose_name='Image')),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='general.Event')),
            ],
        ),
        migrations.DeleteModel(
            name='EventName',
        ),
    ]