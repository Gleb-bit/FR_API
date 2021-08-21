# Generated by Django 3.2.6 on 2021-08-21 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0023_question_all_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='passage_user_id',
        ),
        migrations.AddField(
            model_name='quiz',
            name='passage_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]