# Generated by Django 4.0.1 on 2022-01-30 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_remove_menuitem_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
