# Generated by Django 3.0.7 on 2020-06-13 03:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('references', '0003_auto_20200613_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='References',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleRf', models.CharField(max_length=250)),
                ('descriptionRf', models.TextField()),
                ('linkRf', models.URLField()),
                ('createdRf', models.DateTimeField()),
                ('updatedRf', models.DateTimeField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('statusRf', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('authorRf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='references_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-titleRf',),
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
