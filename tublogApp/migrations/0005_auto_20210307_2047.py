# Generated by Django 3.1.7 on 2021-03-07 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tublogApp', '0004_auto_20210306_2208'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posteo',
            new_name='Post',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
