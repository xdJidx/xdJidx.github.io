# Generated by Django 4.2.6 on 2023-11-02 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournois', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='age',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='equipe',
        ),
    ]