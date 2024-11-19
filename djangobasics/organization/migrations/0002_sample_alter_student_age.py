# Generated by Django 5.1.3 on 2024-11-14 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField()),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('price', models.FloatField()),
                ('amout', models.DecimalField(decimal_places=2, max_digits=10)),
                ('appointment_time', models.TimeField(auto_now=True)),
                ('email', models.EmailField(max_length=20)),
                ('url', models.URLField()),
                ('files', models.FileField(upload_to='files/')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(),
        ),
    ]
