# Generated by Django 3.0.8 on 2020-10-11 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField()),
                ('question_text', models.TextField(blank=True, null=True)),
                ('answer_type', models.CharField(choices=[('1', 'values'), ('2', 'yes_or_no')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_number', models.IntegerField()),
                ('answer_type', models.CharField(choices=[('1', 'values'), ('2', 'yes_or_no')], max_length=10)),
                ('answer_value', models.IntegerField(blank=True, null=True)),
                ('yes_or_no', models.CharField(blank=True, max_length=5, null=True)),
                ('answer_text', models.TextField(blank=True, null=True)),
                ('answer_date', models.DateTimeField(auto_now=True)),
                ('answer_test', models.IntegerField()),
                ('answer_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-answer_date'],
            },
        ),
    ]
