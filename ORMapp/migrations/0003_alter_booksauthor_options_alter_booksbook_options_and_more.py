# Generated by Django 5.0.3 on 2024-03-16 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ORMapp', '0002_alter_booksauthor_options_alter_booksbook_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booksauthor',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='booksbook',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='booksbookauthors',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='booksbookbookshelves',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='booksbooklanguages',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='booksbookshelf',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='booksbooksubjects',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='booksformat',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='bookslanguage',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='bookssubject',
            options={'managed': False},
        ),
    ]
