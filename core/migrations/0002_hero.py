# Generated by Django 5.2 on 2025-04-22 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text="e.g. Hi, I'm XYZ.", max_length=200)),
                ('subtitle', models.CharField(help_text='e.g. A Full-Stack Web Developer.', max_length=200)),
                ('intro', models.TextField(help_text='Short intro paragraph.')),
                ('profile_image', models.ImageField(help_text='Hero image.', upload_to='hero/')),
                ('cv', models.FileField(blank=True, help_text='Downloadable CV', null=True, upload_to='cv/')),
            ],
        ),
    ]
