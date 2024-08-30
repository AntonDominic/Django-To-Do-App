# Generated by Django 5.0.7 on 2024-08-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('description', models.TextField(blank=True, null=True)),
                ('due_date', models.DateField()),
                ('due_time', models.TimeField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
