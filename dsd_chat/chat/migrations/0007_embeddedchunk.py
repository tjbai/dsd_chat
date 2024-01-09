# Generated by Django 5.0.1 on 2024-01-09 01:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_alter_chat_date_chatted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmbeddedChunk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('summary', models.CharField(max_length=1000000)),
                ('raw_chunk', models.CharField(max_length=1000000)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.document')),
            ],
        ),
    ]
