# Generated by Django 3.0.3 on 2020-02-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20200224_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='benefits',
            field=models.TextField(blank=True, default=''),
        ),
    ]
