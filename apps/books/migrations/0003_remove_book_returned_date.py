# Generated by Django 5.0.6 on 2024-07-27 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_returned_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='returned_date',
        ),
    ]
