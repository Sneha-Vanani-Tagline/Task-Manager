from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)      # it automatically calls the set_passsword method
    
