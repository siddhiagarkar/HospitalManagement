# Generated by Django 4.0.4 on 2022-06-18 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosp', '0004_rename_name_patient_info_firstname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient_info',
            old_name='firstname',
            new_name='name',
        ),
    ]
