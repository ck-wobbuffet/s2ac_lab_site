# Generated by Django 2.0 on 2020-06-20 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2aclab', '0007_auto_20200605_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
