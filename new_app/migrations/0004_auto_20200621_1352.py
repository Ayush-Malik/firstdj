# Generated by Django 3.0.7 on 2020-06-21 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0003_auto_20200621_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=122, null=True),
        ),
    ]
