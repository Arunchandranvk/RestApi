# Generated by Django 4.1.7 on 2023-04-02 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genere', models.CharField(max_length=100)),
                ('mainincredient', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]