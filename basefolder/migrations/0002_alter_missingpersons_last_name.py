# Generated by Django 4.1.7 on 2023-04-10 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basefolder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingpersons',
            name='last_name',
            field=models.CharField(max_length=15),
        ),
    ]