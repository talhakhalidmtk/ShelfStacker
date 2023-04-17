from django.db import models
from account.models import User


class Publisher(models.Model):
    name = models.CharField(
        max_length=50, help_text="The name of the Publisher.")
    website = models.URLField(help_text="The Publisher's website.")
    email = models.EmailField(help_text="The Publisher's email address.")

    def __str__(self):
        return self.name


class Rack(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the rack name")
    location = models.CharField(
        max_length=100, help_text="Enter the location of the rack")
    capacity = models.PositiveIntegerField(
        help_text="Enter the maximum number of books that can be stored in the rack")

    def __str__(self):
        return self.name


class Book(models.Model):
    CATEGORY_CHOICES = (
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-fiction'),
        ('science', 'Science'),
        ('history', 'History'),
        ('art', 'Art'),
    )
    title = models.CharField(max_length=70, help_text="The title of the book.")
    isbn = models.CharField(max_length=13, unique=True,
                            help_text="The ISBN number of the book.")
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        help_text="The category of the book.")
    rack = models.ForeignKey(Rack, on_delete=models.SET_NULL, null=True)
    publication_date = models.DateField(
        verbose_name="Date the book was published.")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(User, through="BookContributor")
    quantity = models.PositiveIntegerField(
        default=0, help_text="The total number of copies of the book.")
    available = models.PositiveIntegerField(
        default=0, help_text="The number of available copies of the book.")

    def __str__(self):
        return self.title


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(
        verbose_name="The role this contributor had in the book.",
        choices=ContributionRole.choices,
        max_length=20)

    def __str__(self):
        return "{} ({})".format(self.contributor, self.role)
