# Generated by Django 4.0 on 2022-08-11 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shredit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shredit',
            name='chucked_file',
            field=models.FileField(upload_to='zipped'),
        ),
    ]
