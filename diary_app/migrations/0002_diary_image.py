# Generated by Django 2.2.1 on 2019-06-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
    ]
