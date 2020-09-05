# Generated by Django 3.1 on 2020-09-02 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Crew',
                'verbose_name_plural': 'Crews',
            },
        ),
        migrations.CreateModel(
            name='Bboy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('points', models.IntegerField()),
                ('crew', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crew', to='bboys.crew')),
            ],
            options={
                'verbose_name': 'Bboy',
                'verbose_name_plural': 'Bboys',
                'unique_together': {('crew',)},
            },
        ),
    ]