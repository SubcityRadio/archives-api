# Generated by Django 2.1.5 on 2019-02-21 12:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0006_auto_20190221_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivepost',
            name='post_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
