# Generated by Django 5.0.6 on 2024-05-28 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default=True, null=True, upload_to='students_images/'),
        ),
    ]