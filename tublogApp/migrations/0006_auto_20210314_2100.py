# Generated by Django 3.1.7 on 2021-03-15 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tublogApp', '0005_auto_20210314_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='descripcion',
            field=models.TextField(blank=True, default='', max_length=1000, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(upload_to='posteos/'),
        ),
    ]
