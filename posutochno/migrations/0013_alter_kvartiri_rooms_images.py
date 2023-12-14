# Generated by Django 4.1.7 on 2023-04-11 09:55

from django.db import migrations, models
import django.db.models.deletion
import posutochno.models


class Migration(migrations.Migration):

    dependencies = [
        ('posutochno', '0012_kvartiri_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kvartiri',
            name='rooms',
            field=models.SmallIntegerField(blank=True, default=1, max_length=1, verbose_name='Количество комнат'),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to=posutochno.models.images_directory_path)),
                ('kv_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='posutochno.kvartiri')),
            ],
        ),
    ]