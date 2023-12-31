# Generated by Django 3.2.16 on 2023-06-16 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20230616_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_cd', models.CharField(max_length=10)),
                ('country_name', models.CharField(max_length=50)),
                ('salary_slab', models.IntegerField()),
                ('tax', models.FloatField()),
                ('gov_leaves', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_cd', models.CharField(max_length=10)),
                ('region_name', models.CharField(max_length=50)),
                ('regional_leaves', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_typ', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
                ('org_leaves', models.IntegerField()),
                ('variables', models.FloatField()),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
            ],
        ),
    ]
