# Generated by Django 5.0.6 on 2024-08-26 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='emai',
            new_name='email',
        ),
    ]
