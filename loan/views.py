from .serializers import LoanSerializer
from rest_framework import serializers
from rest_framework.response import Response
from catalog.views import GenericModelViewSet


class LoanViewSet(GenericModelViewSet):
    serializer_class = LoanSerializer

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        quantity = serializer.validated_data['quantity']
        if book.available <= quantity:
            raise serializers.ValidationError("The required copies of this book are not available.")

        member = serializer.validated_data['member']

        if member.books_borrowed() + quantity >= member.max_books_allowed:
            raise serializers.ValidationError("You have reached your max limit.")

        serializer.save()

        # Update the available quantity field in the Book model
        book.available -= quantity
        book.save(update_fields=['available'])

        return Response(serializer.data)

    def perform_update(self, serializer):
        loan = serializer.instance
        quantity = serializer.validated_data['quantity']

        # Update the available_quantity field in the Book model
        book = loan.book
        book.available += quantity
        book.save(update_fields=['available'])

        return Response(serializer.data)
