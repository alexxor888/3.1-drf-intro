# Generated by Django 4.2.4 on 2023-08-31 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Temperature')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date and time')),
                ('photo', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'Measure',
                'verbose_name_plural': 'Measures',
            },
        ),
        migrations.AlterModelOptions(
            name='sensor',
            options={'verbose_name': 'Sensor', 'verbose_name_plural': 'Sensors'},
        ),
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Name'),
        ),
        migrations.DeleteModel(
            name='Measurement',
        ),
        migrations.AddField(
            model_name='measure',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='measurements', to='measurement.sensor', verbose_name='Sensor'),
        ),
    ]
