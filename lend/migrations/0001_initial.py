# Generated by Django 4.2 on 2023-04-12 09:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membership', '0001_initial'),
        ('catalog', '0003_book_rack'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('date_borrowed', models.DateField(default=django.utils.timezone.now)),
                ('date_due', models.DateField(blank=True, null=True)),
                ('date_returned', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.book')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='membership.membership')),
            ],
            options={
                'ordering': ['-date_borrowed'],
            },
        ),
    ]
