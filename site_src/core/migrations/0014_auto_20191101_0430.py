# Generated by Django 2.2 on 2019-10-31 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_events'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='itemId',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='userId',
            new_name='user',
        ),
    ]
