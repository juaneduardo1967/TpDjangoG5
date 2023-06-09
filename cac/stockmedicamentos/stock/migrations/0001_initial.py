# Generated by Django 4.2 on 2023-04-19 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
                ('fecha_vencimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField()),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.medicamento')),
            ],
        ),
        migrations.AddField(
            model_name='medicamento',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.proveedor'),
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField()),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.medicamento')),
            ],
        ),
    ]
