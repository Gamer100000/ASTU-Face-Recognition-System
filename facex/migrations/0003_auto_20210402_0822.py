# Generated by Django 3.1.5 on 2021-04-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facex', '0002_student_cafe_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cafe_status',
            field=models.CharField(choices=[('C', 'Cafe'), ('NC', 'None Cafe')], max_length=2),
        ),
    ]