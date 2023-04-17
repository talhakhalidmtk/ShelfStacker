from rest_framework import viewsets
from .serializers import BookSerializer, BookContributorSerializer, PublisherSerializer, RackSerializer
from rest_framework.permissions import AllowAny


class GenericModelViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        model = self.serializer_class.Meta.model
        queryset = model.objects.all()
        return queryset

    def get_permissions(self):
        if self.action == 'list':
            # Allow anonymous access to the list action
            permission_classes = [AllowAny]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]


class BookContributorViewSet(GenericModelViewSet):
    serializer_class = BookContributorSerializer


class PublisherViewSet(GenericModelViewSet):
    serializer_class = PublisherSerializer


class BookViewSet(GenericModelViewSet):
    serializer_class = BookSerializer


class RackViewSet(GenericModelViewSet):
    serializer_class = RackSerializer
