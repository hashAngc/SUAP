# Generated by Django 4.1.2 on 2022-10-25 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0013_alter_casos_id_comple_info_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="asignaciontarea",
            name="detalle",
            field=models.TextField(db_column="detalle", default=""),
        ),
    ]
