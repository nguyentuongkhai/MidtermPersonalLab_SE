# Generated by Django 4.0.3 on 2022-04-22 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
    ]
