# Generated by Django 4.2.6 on 2023-10-24 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id_tutorial', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField(verbose_name='descripción')),
                ('estado', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'tutorial',
                'verbose_name_plural': 'tutoriales',
                'db_table': 'Tutorial',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
                'db_table': 'Usuario',
            },
        ),
        migrations.CreateModel(
            name='DetallesTutorial',
            fields=[
                ('id_detalles', models.AutoField(primary_key=True, serialize=False)),
                ('dia_creacion', models.DateTimeField(auto_now_add=True, verbose_name='día de creación')),
                ('id_tutorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tutorial', verbose_name='tutorial')),
                ('usuario_creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario', verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'detalles del tutorial',
                'verbose_name_plural': 'detalles de los tutoriales',
                'db_table': 'DetallesTutorial',
            },
        ),
    ]
