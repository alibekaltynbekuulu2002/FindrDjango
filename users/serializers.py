from rest_framework.serializers import ModelSerializer
from .models import User, UserAddress, UserPayment


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserAddressSerializer(ModelSerializer):
    class Meta:
        model = UserAddress
        fields = "__all__"


class UserPaymentSerializer(ModelSerializer):
    class Meta:
        model = UserPayment
        fields = "__all__"
