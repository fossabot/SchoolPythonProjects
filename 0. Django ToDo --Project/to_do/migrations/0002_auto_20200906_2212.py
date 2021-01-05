# Generated by Django 3.1 on 2020-09-06 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='is_done',
        ),
        migrations.AlterField(
            model_name='todo',
            name='data',
            field=models.CharField(help_text='Insert Content Here.', max_length=255, verbose_name='Reminders'),
        ),
    ]