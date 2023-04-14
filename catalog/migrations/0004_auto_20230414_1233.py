from django.db import migrations
from django.core.exceptions import ObjectDoesNotExist


def add_initial_data(apps, schema_editor):
    User = apps.get_model('account', 'User')
    Publisher = apps.get_model('catalog', 'Publisher')
    Rack = apps.get_model('catalog', 'Rack')
    Book = apps.get_model('catalog', 'Book')
    BookContributor = apps.get_model('catalog', 'BookContributor')

    # Add Publishers
    p1 = Publisher(name='Publisher 1', website='https://publisher1.com', email='publisher1@publisher.com')
    p1.save()
    p2 = Publisher(name='Publisher 2', website='https://.publisher2.com', email='publisher2@publisher.com')
    p2.save()

    # Add Racks
    r1 = Rack(name='Rack 1', location='Location 1', capacity=50)
    r1.save()
    r2 = Rack(name='Rack 2', location='Location 2', capacity=75)
    r2.save()

    # Add Books
    b1 = Book(title='Book 1', isbn='1234567890123', category='fiction', rack=r1, publication_date='2022-01-01',
              publisher=p1, quantity=100, available=100)
    b1.save()
    b2 = Book(title='Book 2', isbn='2345678901234', category='non-fiction', rack=r2, publication_date='2022-02-01',
              publisher=p2, quantity=75, available=75)
    b2.save()

    # Add Book Contributors
    try:
        user1 = User.objects.get(email='user1@example.com')
    except ObjectDoesNotExist:
        user1 = User.objects.create(email='user1@example.com', password='password1')
    try:
        user2 = User.objects.get(email='user2@example.com')
    except ObjectDoesNotExist:
        user2 = User.objects.create(email='user2@example.com', password='password2')

    bc1 = BookContributor(book=b1, contributor=user1, role='AUTHOR')
    bc1.save()
    bc2 = BookContributor(book=b2, contributor=user2, role='EDITOR')
    bc2.save()


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0003_book_rack'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
