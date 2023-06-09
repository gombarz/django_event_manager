# Generated by Django 4.1.3 on 2023-04-25 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='min_group',
            field=models.IntegerField(choices=[(2, 'small group'), (5, 'medium group'), (10, 'big group'), (20, 'large group'), (0, 'no limit')], default=0),
            preserve_default=False,
        ),
    ]
