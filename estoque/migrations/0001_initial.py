# Generated by Django 5.0.1 on 2024-01-20 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('preco', models.FloatField()),
                ('validade', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField()),
            ],
        ),
    ]
