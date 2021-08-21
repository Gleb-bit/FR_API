# Generated by Django 3.2.6 on 2021-08-17 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210817_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('текст', 'ответ текстом'), ('один вариант', 'ответ с выбором одного варианта'), ('несколько вариантов', 'ответ с выбором нескольких вариантов')], default='текст', max_length=255),
        ),
        migrations.DeleteModel(
            name='TypeQuestion',
        ),
    ]