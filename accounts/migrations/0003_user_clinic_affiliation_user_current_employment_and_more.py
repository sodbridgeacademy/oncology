# Generated by Django 4.2.1 on 2023-07-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_user_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="clinic_affiliation",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="current_employment",
            field=models.CharField(
                choices=[("Private", "Private"), ("Government", "Government")],
                max_length=200,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="medical_degree",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="medical_license_number",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="professional_certifications",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="specialty",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="years_of_experience",
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
