# Generated by Django 3.1.7 on 2022-07-01 03:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RentOwner',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('contactnumber', models.CharField(max_length=13)),
            ],
            options={
                'db_table': 'RentOwner',
            },
        ),
        migrations.CreateModel(
            name='Sharee',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('contactnumber', models.CharField(max_length=13)),
            ],
            options={
                'db_table': 'Sharee',
            },
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('coordinates', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('owner', models.ForeignKey(db_column='owner', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.rentowner')),
            ],
            options={
                'db_table': 'Spaces',
            },
        ),
        migrations.CreateModel(
            name='SpaceImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100, null=True)),
                ('caption', models.CharField(max_length=100, null=True)),
                ('space', models.ForeignKey(db_column='space', on_delete=django.db.models.deletion.CASCADE, to='database.space')),
            ],
            options={
                'db_table': 'Images',
            },
        ),
        migrations.CreateModel(
            name='ShareeRenteeRequest',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('contactnumber', models.CharField(max_length=13)),
                ('requestdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('sharee', models.ForeignKey(db_column='sharee', on_delete=django.db.models.deletion.CASCADE, to='database.sharee')),
            ],
            options={
                'db_table': 'ShareeRenteeRequest',
            },
        ),
        migrations.AddField(
            model_name='sharee',
            name='space',
            field=models.ForeignKey(db_column='space', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.space'),
        ),
        migrations.CreateModel(
            name='RentOwnerRenteeRequest',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('contactnumber', models.CharField(max_length=13)),
                ('requestdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('rentowner', models.ForeignKey(db_column='rentowner', on_delete=django.db.models.deletion.CASCADE, to='database.rentowner')),
            ],
            options={
                'db_table': 'RentOwnerRenteeRequest',
            },
        ),
    ]
