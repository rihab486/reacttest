# Generated by Django 4.1.7 on 2023-02-24 02:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_alter_article_validité'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='validité',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 2, 24, 3, 39, 30, 524326), null=True),
        ),
    ]
