# Generated by Django 4.1.7 on 2023-04-02 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posutochno', '0007_kvartiri_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kvartiri',
            options={'ordering': ['?'], 'verbose_name': 'Квартиру', 'verbose_name_plural': 'Квартиры'},
        ),
        migrations.AlterField(
            model_name='kvartiri',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kvartiri',
            name='main_image',
            field=models.ImageField(upload_to='media/kvartiri/main_pics/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='kvartiri',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='kvartiri',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
