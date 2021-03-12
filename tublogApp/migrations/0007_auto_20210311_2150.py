# Generated by Django 3.1.7 on 2021-03-12 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tublogApp', '0006_auto_20210311_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.TextField(default='', max_length=150, verbose_name='Mensaje')),
            ],
        ),
        migrations.AlterModelOptions(
            name='contacto',
            options={'verbose_name': 'Contacto', 'verbose_name_plural': 'Contactos'},
        ),
        migrations.AddField(
            model_name='post',
            name='cantidad_comentarios',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='apellido',
            field=models.CharField(default='', max_length=50, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='asunto',
            field=models.CharField(default='', max_length=50, verbose_name='Asunto'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='mensaje',
            field=models.TextField(default='', max_length=500, verbose_name='Mensaje'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nombre',
            field=models.CharField(default='', max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='descripcion',
            field=models.TextField(blank=True, default='', max_length=100, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(default='', max_length=20, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='post',
            name='comentario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tublogApp.comentario'),
        ),
    ]
