from .models import Lend
from catalog.models import Book
from membership.models import Membership
from rest_framework import serializers


class LendSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    member = serializers.PrimaryKeyRelatedField(queryset=Membership.objects.all())

    class Meta:
        model = Lend
        fields = '__all__'

    def validate(self, data):
        book = data['book']
        quantity = data['quantity']
        member = data['member']

        # Check if required copies of the book are available
        if book.available <= quantity:
            raise serializers.ValidationError("The required copies of this book are not available.")

        # Check if the member has reached the max books allowed limit
        if member.books_borrowed() + quantity >= member.max_books_allowed:
            raise serializers.ValidationError("You have reached your max limit.")

        return data
