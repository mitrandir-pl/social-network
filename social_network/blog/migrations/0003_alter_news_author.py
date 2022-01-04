# Generated by Django 4.0 on 2022-01-04 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_userapi_password'),
        ('blog', '0002_delete_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to='user.userapi'),
        ),
    ]