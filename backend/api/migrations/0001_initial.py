# Generated by Django 4.0.6 on 2022-07-19 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('cel', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=30, null=True)),
                ('instagram', models.CharField(blank=True, max_length=30, null=True)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=80, null=True)),
                ('obs', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(blank=True, max_length=80, null=True)),
                ('projectDescription', models.TextField(blank=True, null=True)),
                ('projectCreatedAt', models.DateField(blank=True, null=True)),
                ('finalUser', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
    ]
