# Generated by Django 5.1.3 on 2024-12-04 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='books_taken',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
