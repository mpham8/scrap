# Generated by Django 5.0.6 on 2024-06-15 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_remove_sharedlist_list_alter_task_todo_list_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='todo_list',
            new_name='shared_list',
        ),
        migrations.AddField(
            model_name='task',
            name='list_type',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
