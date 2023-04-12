from account.models import User
from rest_framework import serializers

from .models import Book, Publisher, BookContributor, Rack


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookContributorSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    contributor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = BookContributor
        fields = '__all__'


class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rack
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    rack = RackSerializer()
    publisher = PublisherSerializer()

    def to_representation(self, instance):
        # Call the parent class's to_representation() method
        representation = super().to_representation(instance)

        contributors = instance.bookcontributor_set.all()
        representation['contributors'] = [
            {
                'name': contributor.contributor.get_full_name(),
                'role': contributor.role
            } for contributor in contributors
        ]

        return representation

    class Meta:
        model = Book
        fields = '__all__'
