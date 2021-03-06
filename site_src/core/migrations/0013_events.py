# Generated by Django 2.2 on 2019-10-31 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0012_auto_20191025_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('event', models.CharField(choices=[('V', 'view'), ('A', 'addtocart'), ('T', 'transaction')], max_length=1)),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Item')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
