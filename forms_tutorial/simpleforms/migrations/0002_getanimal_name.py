# Generated by Django 2.2.4 on 2019-08-15 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleforms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='getanimal',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]