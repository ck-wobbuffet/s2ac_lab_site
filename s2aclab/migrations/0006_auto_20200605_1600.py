# Generated by Django 2.0 on 2020-06-05 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2aclab', '0005_auto_20200605_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='readnum',
            old_name='artilce',
            new_name='article',
        ),
    ]
