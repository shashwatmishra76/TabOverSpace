# Generated by Django 2.1 on 2019-01-01 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0004_subdomain_track'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.Track'),
        ),
    ]
