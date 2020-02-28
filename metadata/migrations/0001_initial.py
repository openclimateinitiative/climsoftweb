# Generated by Django 2.2.7 on 2020-02-24 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obselement',
            fields=[
                ('elementid', models.BigIntegerField(db_column='elementId', primary_key=True, serialize=False)),
                ('abbreviation', models.CharField(blank=True, max_length=255, null=True)),
                ('elementname', models.CharField(blank=True, db_column='elementName', max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('elementscale', models.DecimalField(blank=True, db_column='elementScale', decimal_places=2, max_digits=8, null=True)),
                ('upperlimit', models.CharField(blank=True, db_column='upperLimit', max_length=255, null=True)),
                ('lowerlimit', models.CharField(blank=True, db_column='lowerLimit', max_length=255, null=True)),
                ('units', models.CharField(blank=True, max_length=255, null=True)),
                ('elementtype', models.CharField(blank=True, max_length=50, null=True)),
                ('qctotalrequired', models.IntegerField(blank=True, db_column='qcTotalRequired', null=True)),
                ('selected', models.IntegerField()),
            ],
            options={
                'db_table': 'obselement',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('stationid', models.CharField(db_column='stationId', max_length=255, primary_key=True, serialize=False)),
                ('stationname', models.CharField(blank=True, db_column='stationName', max_length=255, null=True)),
                ('wmoid', models.CharField(blank=True, max_length=20, null=True)),
                ('icaoid', models.CharField(blank=True, max_length=20, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('qualifier', models.CharField(blank=True, max_length=20, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('elevation', models.CharField(blank=True, max_length=255, null=True)),
                ('geolocationmethod', models.CharField(blank=True, db_column='geoLocationMethod', max_length=255, null=True)),
                ('geolocationaccuracy', models.FloatField(blank=True, db_column='geoLocationAccuracy', null=True)),
                ('openingdatetime', models.CharField(blank=True, db_column='openingDatetime', max_length=50, null=True)),
                ('closingdatetime', models.CharField(blank=True, db_column='closingDatetime', max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('authority', models.CharField(blank=True, max_length=255, null=True)),
                ('adminregion', models.CharField(blank=True, db_column='adminRegion', max_length=255, null=True)),
                ('drainagebasin', models.CharField(blank=True, db_column='drainageBasin', max_length=255, null=True)),
                ('wacaselection', models.IntegerField(blank=True, db_column='wacaSelection', null=True)),
                ('cptselection', models.IntegerField(blank=True, db_column='cptSelection', null=True)),
                ('stationoperational', models.IntegerField(blank=True, db_column='stationOperational', null=True)),
            ],
            options={
                'db_table': 'station',
                'managed': True,
            },
        ),
    ]
