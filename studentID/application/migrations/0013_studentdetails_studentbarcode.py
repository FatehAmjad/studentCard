# Generated by Django 4.2.2 on 2023-07-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_alter_studentdetails_studentimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='studentBarcode',
            field=models.ImageField(blank=True, null=True, upload_to='cardBarcode/'),
        ),
    ]
