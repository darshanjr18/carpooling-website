# Generated by Django 5.0.7 on 2024-08-06 19:35

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='seats_booked',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='car_model',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='route',
        ),
        migrations.RemoveField(
            model_name='route',
            name='distance',
        ),
        migrations.RemoveField(
            model_name='route',
            name='end_location',
        ),
        migrations.RemoveField(
            model_name='route',
            name='start_location',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='route',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.route'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='driver',
            name='vehicle_details',
            field=models.TextField(default='no details provided', max_length=255),
        ),
        migrations.AddField(
            model_name='route',
            name='arrival_location',
            field=models.CharField(default='#location not known', max_length=255),
        ),
        migrations.AddField(
            model_name='route',
            name='arrival_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='route',
            name='departure_location',
            field=models.CharField(default='#location now known', max_length=255),
        ),
        migrations.AddField(
            model_name='route',
            name='departure_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
