# Generated by Django 4.0.4 on 2022-06-14 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hosp', '0002_choose'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('datecreated', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='choose',
            name='name',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.DeleteModel(
            name='Choose',
        ),
        migrations.DeleteModel(
            name='Username',
        ),
    ]
