# Generated by Django 3.0.8 on 2020-08-01 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200801_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='au_email',
            new_name='email',
        ),
    ]
