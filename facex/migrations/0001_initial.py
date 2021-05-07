# Generated by Django 3.1.5 on 2021-04-11 06:54

import django.db.models.deletion
import django.utils.timezone
import smart_selects.db_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FieldOfStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_of_study', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=120)),
                ('field_of_study', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='school_program', chained_model_field='school_program', on_delete=django.db.models.deletion.CASCADE, to='facex.fieldofstudy')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_program', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StudentLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_history', models.FileField(upload_to='media/logs/%y/%m')),
                ('log_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(unique=True, upload_to='images/face_datas')),
                ('id_n', models.CharField(max_length=12, unique=True)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('cafe_status', models.CharField(choices=[('C', 'Cafe'), ('NC', 'None Cafe')], max_length=2)),
                ('year_of_study', models.CharField(choices=[('FM', 'Freshman'), ('SO', 'Sopomer'), ('JU', 'Juniour'), ('SE', 'Senior'), ('GC', 'GC')], max_length=2)),
                ('department', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='school', chained_model_field='school', on_delete=django.db.models.deletion.CASCADE, to='facex.department')),
                ('field_of_study', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='school_program', chained_model_field='school_program', on_delete=django.db.models.deletion.CASCADE, to='facex.fieldofstudy')),
                ('school', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='field_of_study', chained_model_field='field_of_study', on_delete=django.db.models.deletion.CASCADE, to='facex.school')),
                ('school_program', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facex.schoolprogram')),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='school_program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facex.schoolprogram'),
        ),
        migrations.AddField(
            model_name='fieldofstudy',
            name='school_program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facex.schoolprogram'),
        ),
        migrations.AddField(
            model_name='department',
            name='field_of_study',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='school_program', chained_model_field='school_program', on_delete=django.db.models.deletion.CASCADE, to='facex.fieldofstudy'),
        ),
        migrations.AddField(
            model_name='department',
            name='school',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='field_of_study', chained_model_field='field_of_study', on_delete=django.db.models.deletion.CASCADE, to='facex.school'),
        ),
        migrations.AddField(
            model_name='department',
            name='school_program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facex.schoolprogram'),
        ),
    ]