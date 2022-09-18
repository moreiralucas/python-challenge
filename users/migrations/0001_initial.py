# Generated by Django 4.1.1 on 2022-09-17 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('zipcode', models.CharField(max_length=16)),
                ('suite', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('street', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('bs', models.CharField(max_length=128)),
                ('catchphrase', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Localization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lng', models.DecimalField(decimal_places=10, max_digits=20)),
                ('lat', models.DecimalField(decimal_places=10, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('website', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=128)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.address')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.company')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='localization',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.localization'),
        ),
    ]
