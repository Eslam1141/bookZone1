# Generated by Django 2.0.2 on 2018-02-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookZone', '0005_auto_20180224_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_pic',
            field=models.ImageField(default='/home/linamasoud/Documents/user.png', upload_to='static/images/authors'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_pic',
            field=models.ImageField(default='/home/linamasoud/Documents/book.png', upload_to='static/images/books'),
        ),
    ]
