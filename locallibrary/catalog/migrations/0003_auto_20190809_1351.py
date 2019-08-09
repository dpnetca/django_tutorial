# Generated by Django 2.2.4 on 2019-08-09 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190809_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On Loan'), ('a', 'Available'), ('r', 'Reservered')], default='m', help_text='Book availability', max_length=1),
        ),
    ]
