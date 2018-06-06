# Generated by Django 2.0.2 on 2018-03-26 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palsbet', '0007_auto_20180324_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='PunterPick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(verbose_name='Date Published')),
                ('country', models.CharField(max_length=200)),
                ('home_team', models.CharField(max_length=200)),
                ('home_score', models.IntegerField(default=0)),
                ('away_score', models.IntegerField(default=0)),
                ('away_team', models.CharField(max_length=200)),
                ('prediction', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Running', 'Running'), ('Won', 'Won'), ('Lost', 'Lost')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RollOver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(verbose_name='Date Published')),
                ('country', models.CharField(max_length=200)),
                ('home_team', models.CharField(max_length=200)),
                ('home_score', models.IntegerField(default=0)),
                ('away_score', models.IntegerField(default=0)),
                ('away_team', models.CharField(max_length=200)),
                ('prediction', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Running', 'Running'), ('Won', 'Won'), ('Lost', 'Lost')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VipTips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(verbose_name='Date Published')),
                ('country', models.CharField(max_length=200)),
                ('home_team', models.CharField(max_length=200)),
                ('home_score', models.IntegerField(default=0)),
                ('away_score', models.IntegerField(default=0)),
                ('away_team', models.CharField(max_length=200)),
                ('prediction', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Running', 'Running'), ('Won', 'Won'), ('Lost', 'Lost')], max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='VipTipsGames',
        ),
    ]