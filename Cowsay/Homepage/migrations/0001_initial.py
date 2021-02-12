# Generated by Django 3.1.6 on 2021-02-11 23:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CowsayDisplay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userInputText', models.CharField(max_length=100)),
                ('publishDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
