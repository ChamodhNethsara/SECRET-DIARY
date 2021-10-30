# Generated by Django 3.2.8 on 2021-10-23 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diary', '0004_remove_diary_note_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary_note',
            name='Diary',
        ),
        migrations.AddField(
            model_name='diary_note',
            name='Owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diary_note',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Diary',
        ),
    ]
