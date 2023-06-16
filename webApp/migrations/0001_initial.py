# Generated by Django 4.1.7 on 2023-05-22 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usersignupDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(blank=True, max_length=100, null=True)),
                ('userEmail', models.EmailField(blank=True, max_length=100, null=True)),
                ('userMobile', models.IntegerField(blank=True, null=True)),
                ('userPassword', models.CharField(blank=True, max_length=100, null=True)),
                ('userImage', models.ImageField(blank=True, null=True, upload_to='userProfile')),
            ],
        ),
    ]
