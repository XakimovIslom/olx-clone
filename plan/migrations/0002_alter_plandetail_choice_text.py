# Generated by Django 5.0.2 on 2024-02-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plandetail',
            name='choice_text',
            field=models.CharField(choices=[('7', 'Select Button'), ('30', 'Select Button2')], max_length=128),
        ),
    ]
