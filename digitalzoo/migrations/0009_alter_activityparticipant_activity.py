# Generated by Django 4.2.7 on 2024-03-16 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("digitalzoo", "0008_activityparticipant_animal_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activityparticipant",
            name="activity",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="digitalzoo.activity",
            ),
        ),
    ]
