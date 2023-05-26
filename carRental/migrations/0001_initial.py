# Generated by Django 3.1.1 on 2022-04-14 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BrandName', models.CharField(max_length=100, null=True)),
                ('Creationdate', models.DateTimeField(auto_now_add=True)),
                ('UpdationDate', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contactusinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=250, null=True)),
                ('EmailId', models.CharField(max_length=100, null=True)),
                ('ContactNo', models.CharField(max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contactusquery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250, null=True)),
                ('EmailId', models.CharField(max_length=100, null=True)),
                ('ContactNo', models.CharField(max_length=12, null=True)),
                ('Message', models.CharField(max_length=250, null=True)),
                ('PostingDate', models.DateTimeField(auto_now_add=True)),
                ('Status', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehiclesTitle', models.CharField(max_length=250, null=True)),
                ('VehiclesBrand', models.CharField(max_length=200, null=True)),
                ('VehiclesOverview', models.CharField(max_length=350, null=True)),
                ('PricePerDay', models.CharField(max_length=200, null=True)),
                ('FuelType', models.CharField(max_length=150, null=True)),
                ('ModelYear', models.CharField(max_length=150, null=True)),
                ('SeatingCapacity', models.CharField(max_length=150, null=True)),
                ('Vimage1', models.FileField(blank=True, null=True, upload_to='')),
                ('Vimage2', models.FileField(blank=True, null=True, upload_to='')),
                ('Vimage3', models.FileField(blank=True, null=True, upload_to='')),
                ('Vimage4', models.FileField(blank=True, null=True, upload_to='')),
                ('Vimage5', models.FileField(blank=True, null=True, upload_to='')),
                ('AirConditioner', models.CharField(max_length=50, null=True)),
                ('PowerDoorLocks', models.CharField(max_length=50, null=True)),
                ('AntiLockBrakingSystem', models.CharField(max_length=50, null=True)),
                ('BrakeAssist', models.CharField(max_length=50, null=True)),
                ('PowerSteering', models.CharField(max_length=50, null=True)),
                ('DriverAirbag', models.CharField(max_length=50, null=True)),
                ('PassengerAirbag', models.CharField(max_length=50, null=True)),
                ('PowerWindows', models.CharField(max_length=50, null=True)),
                ('CDPlayer', models.CharField(max_length=50, null=True)),
                ('CentralLocking', models.CharField(max_length=50, null=True)),
                ('CrashSensor', models.CharField(max_length=50, null=True)),
                ('LeatherSeats', models.CharField(max_length=50, null=True)),
                ('RegDate', models.DateTimeField(auto_now_add=True)),
                ('UpdationDate', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ContactNo', models.CharField(max_length=12, null=True)),
                ('dob', models.DateField(null=True)),
                ('Address', models.CharField(max_length=250, null=True)),
                ('City', models.CharField(max_length=150, null=True)),
                ('Country', models.CharField(max_length=100, null=True)),
                ('RegDate', models.DateTimeField(auto_now_add=True)),
                ('UpdationDate', models.DateField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookingNumber', models.CharField(max_length=150, null=True)),
                ('FromDate', models.DateField(null=True)),
                ('ToDate', models.DateField(null=True)),
                ('message', models.CharField(max_length=350, null=True)),
                ('Status', models.CharField(max_length=150, null=True)),
                ('PostingDate', models.DateTimeField(auto_now_add=True)),
                ('LastUpdationDate', models.DateField(null=True)),
                ('VehicleId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carRental.vehicles')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
