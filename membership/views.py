from catalog.views import GenericModelViewSet
from .serializers import MemberSerializer


class MembershipViewSet(GenericModelViewSet):
    serializer_class = MemberSerializer
