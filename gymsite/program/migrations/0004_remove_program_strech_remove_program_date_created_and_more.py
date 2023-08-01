# Generated by Django 4.2.3 on 2023-07-25 19:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('program', '0003_remove_userprofile_wight_userprofile_birth_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='Strech',
        ),
        migrations.RemoveField(
            model_name='program',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='program',
            name='excercize',
        ),
        migrations.AddField(
            model_name='program',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='excercize',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='excercize_pics'),
        ),
        migrations.AlterField(
            model_name='strech',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='strech_pics'),
        ),
        migrations.CreateModel(
            name='ProgramDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('date_created', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('excercize', models.ManyToManyField(to='program.excercize')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.program')),
                ('strech', models.ManyToManyField(to='program.strech')),
            ],
        ),
        migrations.AddField(
            model_name='program',
            name='days',
            field=models.ManyToManyField(related_name='program_days', to='program.programday'),
        ),
    ]