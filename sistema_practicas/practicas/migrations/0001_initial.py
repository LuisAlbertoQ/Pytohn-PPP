# Generated by Django 5.1.1 on 2024-09-16 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('representante', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrera', models.CharField(max_length=100)),
                ('semestre', models.IntegerField()),
                ('universidad', models.CharField(max_length=100)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('rol', models.CharField(choices=[('admin', 'Admin'), ('estudiante', 'Estudiante'), ('supervisor', 'Supervisor'), ('empresa', 'Empresa')], max_length=20)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='practicas.empresa')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='practicas.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Practica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('horas_totales', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('en curso', 'En curso'), ('completada', 'Completada')], default='pendiente', max_length=20)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='practicas.empresa')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practicas.estudiante')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='practicas.supervisor')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_evaluacion', models.DateField()),
                ('calificacion', models.DecimalField(decimal_places=2, max_digits=4)),
                ('comentarios', models.TextField()),
                ('practica', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='practicas.practica')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practicas.supervisor')),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='practicas.usuario'),
        ),
    ]
