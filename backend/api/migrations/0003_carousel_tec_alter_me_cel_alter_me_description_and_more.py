# Generated by Django 4.0.6 on 2022-07-24 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_project_produtimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carTitle', models.CharField(blank=True, max_length=80, null=True)),
                ('carImg', models.ImageField(blank=True, null=True, upload_to='')),
                ('carText', models.CharField(blank=True, max_length=500, null=True)),
                ('carSubText', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tecName', models.CharField(blank=True, max_length=80, null=True)),
                ('tecLogo', models.ImageField(blank=True, null=True, upload_to='')),
                ('tecText', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='me',
            name='cel',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='me',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='me',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='me',
            name='instagram',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='me',
            name='linkedin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='me',
            name='obs',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
