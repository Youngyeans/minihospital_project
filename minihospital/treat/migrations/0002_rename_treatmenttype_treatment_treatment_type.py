# Generated by Django 5.1.1 on 2024-10-12 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treatment',
            old_name='treatmentType',
            new_name='treatment_type',
        ),
    ]
