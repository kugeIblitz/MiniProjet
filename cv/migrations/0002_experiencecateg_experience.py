# Generated by Django 4.1.4 on 2022-12-10 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceCateg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'ExperienceCateg',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_name', models.CharField(max_length=20)),
                ('experienceCateg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.experiencecateg')),
            ],
        ),
    ]
