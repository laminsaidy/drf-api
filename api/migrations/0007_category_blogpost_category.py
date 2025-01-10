# Generated by Django 5.1.4 on 2025-01-09 14:14

import django.db.models.deletion
from django.db import migrations, models

def set_default_category(apps, schema_editor):
    Category = apps.get_model('api', 'Category')
    default_category = Category.objects.first()  # Get the first category (assuming it exists)
    BlogPost = apps.get_model('api', 'BlogPost')
    BlogPost.objects.update(category=default_category)  # Update all BlogPosts to have this category


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_vote_unique_together_remove_vote_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to='api.category',
            ),
        ),
        migrations.RunPython(set_default_category),
    ]