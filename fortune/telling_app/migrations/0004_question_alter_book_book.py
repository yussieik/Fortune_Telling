# Generated by Django 4.2.4 on 2023-09-02 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telling_app', '0003_alter_quotes_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='book',
            field=models.CharField(max_length=100, null=True),
        ),
    ]