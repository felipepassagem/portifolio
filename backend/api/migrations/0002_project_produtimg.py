# Generated by Django 4.0.6 on 2022-07-22 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='produtImg',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
