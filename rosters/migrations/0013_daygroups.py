# Generated by Django 2.2.3 on 2019-07-18 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0012_daygroups'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='day_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rosters.DayGroup'),
        ),
        migrations.AddField(
            model_name='staffrule',
            name='day_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rosters.DayGroup'),
        ),
    ]
