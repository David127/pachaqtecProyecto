# Generated by Django 3.1.7 on 2021-08-03 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Cupones',
            },
        ),
        migrations.CreateModel(
            name='BlackListedCupon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cupon_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cupon.cupon')),
            ],
        ),
    ]