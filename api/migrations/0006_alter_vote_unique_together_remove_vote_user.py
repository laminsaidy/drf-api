# Generated by Django 5.1.4 on 2025-01-08 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_comment"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="vote",
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name="vote",
            name="user",
        ),
    ]
