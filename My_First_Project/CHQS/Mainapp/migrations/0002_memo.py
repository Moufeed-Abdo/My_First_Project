# Generated by Django 2.2.5 on 2020-07-16 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mem_sora', models.CharField(max_length=50)),
                ('mem_from', models.IntegerField()),
                ('mem_to', models.IntegerField()),
                ('mem_date', models.DateField()),
                ('mem_quant', models.IntegerField()),
                ('mem_rmrk', models.CharField(max_length=20)),
                ('mem_finished', models.CharField(max_length=50)),
                ('mem_stu_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='Mainapp.Student')),
            ],
        ),
    ]
