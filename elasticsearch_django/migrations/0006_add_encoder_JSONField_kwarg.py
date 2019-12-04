# Generated by Django 1.11a1 on 2017-04-06 14:40

from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("elasticsearch_django", "0005_convert_JSONFields")]

    operations = [
        migrations.AlterField(
            model_name="searchquery",
            name="hits",
            field=JSONField(
                encoder=DjangoJSONEncoder,
                help_text="The list of meta info for each of the query matches returned.",
            ),
        ),
        migrations.AlterField(
            model_name="searchquery",
            name="query",
            field=JSONField(
                encoder=DjangoJSONEncoder, help_text="The raw ElasticSearch DSL query."
            ),
        ),
    ]
