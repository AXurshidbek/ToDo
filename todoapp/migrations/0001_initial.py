# Generated by Django 4.2.7 on 2023-11-09 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=55)),
                ('batafsil', models.TextField()),
                ('sana', models.DateField()),
                ('holati', models.CharField(choices=[('Bajarilyapti', 'Bajarilyapti'), ('Bajarilmadi', 'Bajarilmadi')], max_length=25)),
            ],
        ),
    ]
