# Generated by Django 2.1 on 2019-02-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcisDB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DutStaticInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usb_ser', models.CharField(max_length=20)),
                ('birthday', models.CharField(max_length=20)),
                ('FSN', models.CharField(max_length=20)),
                ('remove_status', models.CharField(max_length=20)),
                ('dead_date', models.CharField(max_length=25)),
                ('slave_mac_addr', models.CharField(max_length=30)),
                ('owner', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SlaveStaticInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_version', models.CharField(max_length=20)),
                ('birthday', models.CharField(max_length=20)),
                ('hostname', models.CharField(max_length=40)),
                ('mac_addr', models.CharField(max_length=45)),
                ('remove_status', models.BooleanField()),
                ('dead_date', models.CharField(max_length=25)),
                ('owner', models.CharField(max_length=30)),
            ],
        ),
    ]
