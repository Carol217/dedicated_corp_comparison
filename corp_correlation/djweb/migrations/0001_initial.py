# Generated by Django 2.1.7 on 2019-03-27 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, default='')),
                ('client_of', models.ManyToManyField(blank=True, related_name='_other_client_of_+', to='djweb.Other')),
                ('competitors', models.ManyToManyField(blank=True, related_name='_other_competitors_+', to='djweb.Other')),
                ('has_clients', models.ManyToManyField(blank=True, related_name='_other_has_clients_+', to='djweb.Other')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, default='')),
                ('client_of', models.ManyToManyField(blank=True, related_name='_user_client_of_+', to='djweb.User')),
                ('competitors', models.ManyToManyField(blank=True, related_name='_user_competitors_+', to='djweb.User')),
                ('has_clients', models.ManyToManyField(blank=True, related_name='_user_has_clients_+', to='djweb.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
