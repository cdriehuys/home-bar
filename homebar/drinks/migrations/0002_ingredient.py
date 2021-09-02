# Generated by Django 3.2.7 on 2021-09-02 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('in_stock', models.BooleanField(default=True)),
            ],
        ),
    ]
