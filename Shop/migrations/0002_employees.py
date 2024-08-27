# Generated by Django 4.2.7 on 2024-02-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=200)),
                ('Lname', models.CharField(max_length=200)),
                ('birth_date', models.DateField()),
                ('salary', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
