# Generated by Django 4.1.2 on 2022-12-21 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CA", "0003_alter_campus_ambassador_date_of_birth"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campus_ambassador",
            name="date_of_birth",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
