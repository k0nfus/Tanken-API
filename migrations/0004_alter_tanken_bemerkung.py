# Generated by Django 4.1.7 on 2023-03-09 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanken', '0003_alter_tanken_datum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tanken',
            name='bemerkung',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]