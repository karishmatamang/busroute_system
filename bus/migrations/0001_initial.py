# Generated by Django 4.1.3 on 2023-02-09 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=250)),
                ('bus_number', models.IntegerField(unique=True)),
                ('number_of_routes', models.IntegerField(null=True)),
            ],
        ),
    ]
