from django.contrib.auth.models import User
from django.db import models


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default='Active', choices=(
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Cancelled', 'Cancelled')
    ))
    fee = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    payment_date = models.DateField(null=True, blank=True)
    is_renewal = models.BooleanField(default=False)
    membership_type = models.CharField(max_length=20, default='Student', choices=(
        ('Student', 'Student'),
        ('Faculty', 'Faculty'),
        ('Alumni', 'Alumni')
    ))
    max_books_allowed = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return f'{self.user.username}\'s Membership'

    def books_borrowed(self):
        return self.loan_set.count()
