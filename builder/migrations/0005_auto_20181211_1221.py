# Generated by Django 2.1.3 on 2018-12-11 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0004_card_card_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='text',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
    ]
