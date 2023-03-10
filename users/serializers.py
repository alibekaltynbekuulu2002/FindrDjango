from .models import User,UserAddress,UserPayment
from rest_framework import serializers
from rest_framework.reverse import reverse


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'


class UserPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPayment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = '__all__'

    def get_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("user-detail",kwargs={'id':obj.id},request=request)
    
    def create(self, validated_data):
        """
        This method will work while it's saving a new user
        It will hash the given password -> instance.set_password(password)
        """
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    