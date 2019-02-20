# Generated by Django 2.0.3 on 2019-02-20 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('post_content', models.TextField()),
                ('post_summary', models.TextField()),
                ('post_image_alt_text', models.TextField()),
            ],
        ),
    ]
