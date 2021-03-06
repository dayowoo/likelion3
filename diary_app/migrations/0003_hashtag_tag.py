# Generated by Django 2.2.1 on 2019-07-03 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary_app', '0002_diary_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary_app.Diary')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='diary_app.Tag')),
            ],
        ),
    ]
