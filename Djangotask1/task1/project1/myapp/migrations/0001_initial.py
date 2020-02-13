# Generated by Django 2.2.10 on 2020-02-11 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hydroponics',
            fields=[
                ('h_id', models.AutoField(primary_key=True, serialize=False)),
                ('plant_name', models.CharField(max_length=255)),
                ('plant_type', models.CharField(max_length=255)),
                ('temperature', models.CharField(max_length=255)),
                ('humidity', models.CharField(max_length=255)),
                ('ph_value', models.CharField(max_length=255)),
                ('motor', models.BooleanField(default='none')),
                ('light', models.BooleanField(default='none')),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('uname', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('DOB', models.DateTimeField(null=True)),
                ('emailId', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='audit_log',
            fields=[
                ('log_Id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.DateTimeField()),
                ('logout', models.DateTimeField()),
                ('activity', models.CharField(max_length=255)),
                ('uname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.profile')),
            ],
        ),
    ]
