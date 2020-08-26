# Generated by Django 3.1 on 2020-08-26 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0024_auto_20200826_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shiftrule',
            name='roles',
            field=models.ManyToManyField(through='rosters.ShiftRuleRole', to='rosters.Role'),
        ),
        migrations.AlterField(
            model_name='shiftrulerole',
            name='shift_rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shift_rule_role_set', to='rosters.shiftrule'),
        ),
    ]
