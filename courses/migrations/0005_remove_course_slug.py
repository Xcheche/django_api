# Generated by Django 5.0.7 on 2024-08-25 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0004_alter_course_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="slug",
        ),
    ]
