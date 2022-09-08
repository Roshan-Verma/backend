# Generated by Django 4.1 on 2022-09-08 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('anwesha_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('college_name', models.CharField(max_length=150)),
                ('profile_photo', models.URLField(blank=True, null=True)),
                ('age', models.SmallIntegerField()),
                ('is_email_verified', models.BooleanField()),
                ('user_type', models.CharField(max_length=10)),
                ('qr_code', models.URLField()),
                ('gender', models.CharField(max_length=20)),
                ('accomadation_selected', models.BooleanField(default=False)),
                ('is_profile_completed', models.BooleanField(default=False)),
                ('instagram_id', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_id', models.CharField(blank=True, max_length=255, null=True)),
                ('time_of_registration', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]