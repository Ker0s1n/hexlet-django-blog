# Generated by Django 5.1.3 on 2024-11-19 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_comment_delete_articlecomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at']},
        ),
    ]