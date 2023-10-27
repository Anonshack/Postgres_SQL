# Generated by Django 4.2.6 on 2023-10-26 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Information')),
                ('year', models.DateField(auto_now_add=True, verbose_name='year')),
                ('info', models.TextField(verbose_name='Information')),
            ],
        ),
    ]