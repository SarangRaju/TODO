# Generated by Django 3.2.23 on 2024-01-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
