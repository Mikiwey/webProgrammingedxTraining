# Generated by Django 4.0.dev20210416091810 on 2022-12-13 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_auction_list_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_list',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='auctions.category'),
        ),
    ]
