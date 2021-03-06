# Generated by Django 3.1.4 on 2021-01-07 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exfd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('FM', 'FeMale')], max_length=10)),
                ('rollno', models.CharField(max_length=10)),
                ('collegename', models.CharField(choices=[('AANM', 'AANM & VVRSR Polytechnic - GDLR'), ('SVGP', 'S.V Govt Polytechnic'), ('AANMR', 'AANM & VVRSR Polytechnic - RJYD')], max_length=7)),
                ('impf', models.ImageField(default='profile.jpeg', upload_to='Profile/')),
                ('d', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('busid', models.CharField(max_length=10)),
                ('busim', models.ImageField(default='bus.jpg', null=True, upload_to='Bus_Image/')),
                ('distance', models.CharField(max_length=10, null=True)),
                ('cost', models.CharField(max_length=15, null=True)),
                ('timmings', models.CharField(max_length=30)),
                ('busclass', models.CharField(choices=[('Pallevellugu', 'Pallevellugu'), ('Express', 'Express'), ('Ultra Deluxe', 'Ultra Deluxe')], max_length=15)),
                ('da', models.DateField(null=True)),
                ('d', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'data',
            },
        ),
    ]
