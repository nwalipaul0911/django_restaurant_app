# Generated by Django 3.2 on 2022-10-05 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('processing', 'processing'), ('shipping', 'shipping'), ('delivered', 'delivered')], default='processing', max_length=20),
        ),
    ]