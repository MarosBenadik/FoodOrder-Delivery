# Generated by Django 4.0.1 on 2022-01-30 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_ordermodel_is_shippped'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]