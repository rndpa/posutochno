# Generated by Django 4.1.7 on 2023-04-05 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posutochno', '0010_remove_kvartiri_perm_pub_kvartiri_pub'),
        ('users', '0002_profile_pub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='pub',
        ),
        migrations.AddField(
            model_name='profile',
            name='perm_pub',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='posutochno.kvartiri', verbose_name='Разрешение на публикацию'),
        ),
    ]
