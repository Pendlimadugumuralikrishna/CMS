# Generated by Django 4.0.4 on 2022-06-15 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('track_id', models.IntegerField(null=True)),
                ('service', models.CharField(default='dtdc', max_length=100)),
            ],
        ),
    ]
