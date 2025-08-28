from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account, Transaction

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})

        user.set_password(password)
        user.save()
        return user

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_number', 'account_name', 'user', 'account_type', 'balance']

    def create(self, validated_data):
        changed_by = self.context.get('changed_by')
        instance = self.Meta.model(**validated_data)
        if changed_by:
            instance._changed_by = changed_by
        instance.save()
        return instance

    def update(self, instance, validated_data):
        changed_by = self.context.get('changed_by')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if changed_by:
            instance._changed_by = changed_by
        instance.save()
        return instance

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'account', 'user', 'transaction_id', 'transaction_type', 'amount', 'category', 'description', 'status', 'remarks']

    def create(self, validated_data):
        changed_by = self.context.get('changed_by')
        instance = self.Meta.model(**validated_data)
        if changed_by:
            instance._changed_by = changed_by
        instance.save()
        return instance

    def update(self, instance, validated_data):
        changed_by = self.context.get('changed_by')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if changed_by:
            instance._changed_by = changed_by
        instance.save()
        return instance
