# Generated by Django 3.1.7 on 2021-03-06 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tublogApp', '0003_auto_20210306_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(max_length=30),
        ),
    ]