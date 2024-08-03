# Generated by Django 5.0.7 on 2024-07-28 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='status',
        ),
        migrations.AddField(
            model_name='receipt',
            name='status',
            field=models.CharField(choices=[('A', 'Ожидание Админа'), ('B', 'Ожидание Пользователя'), ('C', 'Ожидание оплаты'), ('D', 'Проверка'), ('R', 'Отказано')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='image',
            field=models.ImageField(null=True, upload_to='receipt/'),
        ),
    ]
