# Generated by Django 3.2.6 on 2021-08-21 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0022_auto_20210821_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='all_answers',
            field=models.CharField(default='', max_length=255),
        ),
    ]
