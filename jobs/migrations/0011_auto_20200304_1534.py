# Generated by Django 3.0.3 on 2020-03-04 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20200301_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_item', to='jobs.Category'),
        ),
    ]