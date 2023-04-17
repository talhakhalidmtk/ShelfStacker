from .serializers import LendSerializer
from rest_framework import serializers
from rest_framework.response import Response
from catalog.views import GenericModelViewSet


class LendViewSet(GenericModelViewSet):
    serializer_class = LendSerializer

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        quantity = serializer.validated_data['quantity']

        # Update the available quantity field in the Book model
        book.available -= quantity
        book.save(update_fields=['available'])

        return Response(serializer.data)

    def perform_update(self, serializer):
        lend = serializer.instance
        quantity = serializer.validated_data['quantity']

        # Update the available_quantity field in the Book model
        book = lend.book
        book.available += quantity
        book.save(update_fields=['available'])

        return Response(serializer.data)
