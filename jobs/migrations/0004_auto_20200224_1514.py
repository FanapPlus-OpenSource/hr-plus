# Generated by Django 3.0.3 on 2020-02-24 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20200224_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='job',
            name='good_to_have',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='job',
            name='qualifications',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='job',
            name='requirements',
            field=models.TextField(blank=True, default=''),
        ),
    ]