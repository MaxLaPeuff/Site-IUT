# Generated by Django 5.0.3 on 2024-05-30 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iut', '0003_memoire_delete_pdffile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('photo', models.ImageField(default='', upload_to='media')),
                ('poste', models.CharField(max_length=200)),
            ],
        ),
    ]
