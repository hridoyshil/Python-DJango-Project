# Generated by Django 4.1.7 on 2023-09-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition_App', '0014_alter_post_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class_in',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='class_in',
            field=models.ManyToManyField(related_name='class_set', to='tuition_App.class_in'),
        ),
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.ManyToManyField(related_name='subject_set', to='tuition_App.subject'),
        ),
    ]