# Generated by Django 4.1.2 on 2022-10-28 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0020_alter_asignaciontarea_fech_registro_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="casos",
            name="id_seguimiento",
            field=models.OneToOneField(
                db_column="id_seguimiento",
                default=0,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="api.seguimiento",
            ),
        ),
    ]