# Generated by Django 5.0 on 2023-12-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='leaders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('birth', models.DateField(null=True)),
                ('death', models.DateField(null=True)),
                ('link', models.URLField()),
                ('image', models.ImageField(null=True, upload_to='')),
                ('summary', models.TextField()),
                ('leader_choices', models.CharField(choices=[('EU', 'European Leaders'), ('IND', 'Indian Leaders'), ('AS', 'Asian Leaders'), ('AMC', 'American Leaders'), ('MYT', 'Mythical Leaders')], max_length=100)),
            ],
        ),
    ]
