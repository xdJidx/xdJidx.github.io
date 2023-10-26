# Generated by Django 4.2.6 on 2023-10-26 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournoi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('lieu', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('equipe', models.CharField(max_length=100)),
                ('tournoi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournois.tournoi')),
            ],
        ),
    ]
