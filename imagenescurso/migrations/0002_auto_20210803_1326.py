# Generated by Django 3.1.7 on 2021-08-03 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
        ('imagenescurso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenescurso',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='curso.curso'),
        ),
    ]