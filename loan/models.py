# Create your models here.
from django.db import models
from django.utils import timezone

from catalog.models import Book
from membership.models import Membership


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    date_borrowed = models.DateField(default=timezone.now)
    date_due = models.DateField(null=True, blank=True)
    date_returned = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-date_borrowed']

    def __str__(self):
        return f'{self.book} ({self.member.user.username})'

    def is_overdue(self):
        return self.date_due and self.date_due < timezone.now().date()

    def get_overdue_days(self):
        if self.is_overdue():
            return (timezone.now().date() - self.date_due).days
        return 0
