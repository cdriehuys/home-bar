# Generated by Django 3.2.7 on 2021-09-02 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0003_drinkrecipe'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drink',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ('name',)},
        ),
    ]