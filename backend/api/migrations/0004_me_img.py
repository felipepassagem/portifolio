# Generated by Django 4.0.6 on 2022-08-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_carousel_tec_alter_me_cel_alter_me_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='me',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]