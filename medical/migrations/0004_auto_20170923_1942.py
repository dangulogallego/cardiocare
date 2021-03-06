# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0003_auto_20170914_0307'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpcionPregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(default='Default', max_length=50)),
                ('valor', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(default='Default', max_length=50)),
                ('valor', models.FloatField(blank=True, null=True)),
                ('opciones', models.ManyToManyField(to='medical.OpcionPregunta')),
            ],
        ),
        migrations.CreateModel(
            name='TipoExamen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Test Asa', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='testasa',
            name='paciente',
        ),
        migrations.RemoveField(
            model_name='examen',
            name='colesterolhdl',
        ),
        migrations.RemoveField(
            model_name='examen',
            name='colesterolldl',
        ),
        migrations.RemoveField(
            model_name='examen',
            name='pas',
        ),
        migrations.RemoveField(
            model_name='examen',
            name='seguimiento',
        ),
        migrations.RemoveField(
            model_name='examen',
            name='trigliceridos',
        ),
        migrations.AddField(
            model_name='examen',
            name='resultado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='examen',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiling.Paciente'),
        ),
        migrations.AlterField(
            model_name='puntajecategoria',
            name='nombre',
            field=models.CharField(default='Default', max_length=50),
        ),
        migrations.DeleteModel(
            name='TestAsa',
        ),
        migrations.AddField(
            model_name='examen',
            name='preguntas',
            field=models.ManyToManyField(blank=True, null=True, to='medical.Pregunta'),
        ),
        migrations.AddField(
            model_name='examen',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medical.TipoExamen'),
        ),
    ]
