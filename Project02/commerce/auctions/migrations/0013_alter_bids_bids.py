# Generated by Django 4.0.dev20210416091810 on 2022-12-18 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_auction_list_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='bids',
            field=models.FloatField(),
        ),
    ]
