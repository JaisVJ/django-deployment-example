# Generated by Django 4.0.4 on 2022-05-03 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0003_rename_firstname_user_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AppTwo.user')),
            ],
        ),
    ]
