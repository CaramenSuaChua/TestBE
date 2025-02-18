from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def validate_login(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Login must be at least 3 characters long.")
        return value
