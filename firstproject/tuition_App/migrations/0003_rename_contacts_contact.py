# Generated by Django 4.1.7 on 2023-09-23 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tuition_App', '0002_contacts_delete_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacts',
            new_name='Contact',
        ),
    ]
