# Generated by Django 3.0.7 on 2020-12-31 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Referencia',
            field=models.URLField(blank=True, null=True),
        ),
    ]