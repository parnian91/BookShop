# Generated by Django 4.2.7 on 2024-02-08 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_fname', models.CharField(max_length=200)),
                ('buyer_lname', models.CharField(max_length=200)),
                ('bought_book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Shop.books')),
            ],
        ),
    ]
