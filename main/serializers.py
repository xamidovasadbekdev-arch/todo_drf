from rest_framework import serializers
from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'phone_number', 'first_name', 'last_name', 'date_of_birth', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}  # Don't send password back in JSON

    # Move this OUTSIDE of class Meta (un-indent one level)
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'phone_number', 'first_name', 'last_name', 'date_of_birth',
                  'date_joined']


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    # def validate(self, attrs):
    #     old_password = attrs.get("old_password")
    #     user = self.context['request'].user
    #     if user.password != old_password:
    #         raise serializers.ValidationError("Wrong password")
    #     user.set_password(attrs['new_password'])
    #     return attrs


class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ["id", "title", "details", "status", "created"]

