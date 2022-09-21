# Generated by Django 4.1 on 2022-09-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchlistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
                ('release_date', models.CharField(max_length=255)),
                ('review', models.TextField()),
                ('watched', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='WatchlistItem',
        ),
    ]
