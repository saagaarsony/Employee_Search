# Generated by Django 4.2 on 2023-10-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptname', models.CharField(max_length=100, verbose_name='Depart name')),
                ('depttype', models.CharField(max_length=100, verbose_name='Department Type')),
                ('deptblock', models.CharField(max_length=100, verbose_name='Department Block')),
            ],
        ),
    ]
