# Generated by Django 4.0.6 on 2022-07-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_displayed',
            field=models.BooleanField(default=False),
        ),
    ]