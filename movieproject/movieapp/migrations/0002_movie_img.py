# Generated by Django 3.2.8 on 2021-11-12 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='abc', upload_to='pics'),
            preserve_default=False,
        ),
    ]
