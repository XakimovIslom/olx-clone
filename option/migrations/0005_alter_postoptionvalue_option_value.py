# Generated by Django 5.0.2 on 2024-02-19 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0004_rename_value_postoptionvalue_option_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postoptionvalue',
            name='option_value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='option.optionvalue'),
        ),
    ]
