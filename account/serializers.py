from rest_framework import serializers

from account.models import Account, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_time', 'transaction_type', 'transaction_status', 'description']


class AccountSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True)

    class Meta:
        model = Account
        fields = ['account_number', 'first_name', 'last_name', 'account_type', 'account_balance', 'transactions']


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user', 'account_number', 'pin', 'account_type']
    # account_number = serializers.CharField(max_length=10)
    # first_name = serializers.CharField(max_length=225)
    # last_name = serializers.CharField(max_length=255)
    # balance = serializers.DecimalField(max_digits=6, decimal_places=2)
    # account_type = serializers.CharField(max_length=10)


class DepositWithdrawSerializer(serializers.Serializer):
    account_number = serializers.CharField(max_length=10)
    amount = serializers.DecimalField(max_digits=20, decimal_places=2)
    pin = serializers.CharField(max_length=4)


class TransferSerializer(serializers.Serializer):
    sender_account = serializers.CharField(max_length=10)
    receiver_account = serializers.CharField(max_length=10)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)

# class BalanceSerializer(serializers.ModelSerializer):




