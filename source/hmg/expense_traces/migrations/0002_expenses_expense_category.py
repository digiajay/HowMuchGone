# Generated by Django 4.0.4 on 2022-06-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_traces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='expense_category',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
