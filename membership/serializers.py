from rest_framework import serializers

from .models import Membership
from account.serializers import UserSerializer


class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Membership
        fields = '__all__'
