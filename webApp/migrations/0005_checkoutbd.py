# Generated by Django 4.2.2 on 2023-06-14 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0004_remove_cartdb_cartimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkoutBD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkoutName', models.CharField(blank=True, max_length=100, null=True)),
                ('checkoutEmail', models.CharField(blank=True, max_length=100, null=True)),
                ('checkoutNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('checkoutAddress', models.CharField(blank=True, max_length=1000, null=True)),
                ('checkoutCountry', models.CharField(blank=True, max_length=100, null=True)),
                ('checkoutState', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
