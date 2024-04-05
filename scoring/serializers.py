from rest_framework import serializers

from .models import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'userrole','password']
        extra_kwargs = {
            'password': {'write_only': True}  # Define write_only for the password field
        }


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'user', 'category', 'status', 'application_date']