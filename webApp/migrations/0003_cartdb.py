# Generated by Django 4.2.1 on 2023-06-07 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0002_contactdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartUserName', models.CharField(blank=True, max_length=100, null=True)),
                ('cartName', models.CharField(blank=True, max_length=100, null=True)),
                ('cartDescription', models.CharField(blank=True, max_length=1000, null=True)),
                ('cartQuandity', models.IntegerField(blank=True, null=True)),
                ('cartPrice', models.IntegerField(blank=True, null=True)),
                ('cartImage', models.ImageField(blank=True, null=True, upload_to='CartImage')),
            ],
        ),
    ]