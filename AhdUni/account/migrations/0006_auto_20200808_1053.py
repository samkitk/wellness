# Generated by Django 2.2.8 on 2020-08-08 05:23

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200806_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='reason',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Peer', 'Peer'), ('Social', 'Social'), ('Self', 'Self'), ('Family', 'Family'), ('Group', 'Group')], max_length=200),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='workout_patterns',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Exercise at home', 'Exercise at home'), ('Gyming', 'Gyming'), ('Cycling', 'Cycling'), ('Walk', 'Walk'), ('Yoga', 'Yoga'), ('Zumba', 'Zumba')], max_length=47),
        ),
    ]