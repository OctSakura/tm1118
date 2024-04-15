# Generated by Django 3.2.6 on 2024-04-12 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.CharField(max_length=5)),
                ('node_loc', models.CharField(max_length=10)),
                ('temp', models.IntegerField()),
                ('hum', models.IntegerField()),
                ('light', models.IntegerField()),
                ('snd', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VenueEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('timeStart', models.TimeField()),
                ('timeEnd', models.TimeField()),
                ('event', models.CharField(max_length=10)),
                ('instructor', models.CharField(max_length=50)),
            ],
        ),
    ]