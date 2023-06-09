# Generated by Django 3.1.1 on 2022-04-16 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carRental', '0006_delete_booking'),
    ]

    operations = [
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
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carRental.userdetails')),
            ],
        ),
    ]
