from .models import Loan
from catalog.models import Book
from membership.models import Membership
from rest_framework import serializers


class LoanSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    member = serializers.PrimaryKeyRelatedField(queryset=Membership.objects.all())

    class Meta:
        model = Loan
        fields = '__all__'
