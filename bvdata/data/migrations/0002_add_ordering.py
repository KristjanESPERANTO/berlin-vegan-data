# Generated by Django 2.0 on 2018-01-30 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("data", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(name="gastro", options={"ordering": ["name"]})
    ]
