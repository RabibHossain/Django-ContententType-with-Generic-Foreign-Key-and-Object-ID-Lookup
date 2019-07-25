# Generated by Django 2.2.1 on 2019-07-17 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_track_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={},
        ),
        migrations.RemoveField(
            model_name='track',
            name='book',
        ),
        migrations.RemoveField(
            model_name='track',
            name='my_order',
        ),
        migrations.CreateModel(
            name='TrackList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('my_order', models.PositiveIntegerField(default=0)),
                ('relation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.Screen')),
                ('track', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.Track')),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
    ]