# Generated by Django 5.0.6 on 2024-05-28 03:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='interests',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hobby',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hobby', to='blog.student'),
        ),
    ]
