# Generated by Django 4.2.7 on 2024-02-08 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_employees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=300)),
                ('publishing_yaer', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Shop.authors')),
            ],
        ),
    ]
