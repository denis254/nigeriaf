# Generated by Django 2.0.2 on 2018-03-22 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palsbet', '0002_viptipsgames'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viptipsgames',
            name='cathegory',
            field=models.CharField(max_length=100),
        ),
    ]
