# Generated by Django 3.2.5 on 2021-07-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lists',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('courseCode', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('description', models.TextField(blank=True)),
                ('status', models.BooleanField()),
                ('deleted_at', models.DateTimeField()),
            ],
        ),
    ]