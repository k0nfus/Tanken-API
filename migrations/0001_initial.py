# Generated by Django 4.1.7 on 2023-03-09 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tanken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('betrag', models.DecimalField(decimal_places=2, max_digits=7)),
                ('datum', models.DateTimeField(auto_now_add=True)),
                ('bemerkung', models.TextField(max_length=200, null=True)),
            ],
        ),
    ]
