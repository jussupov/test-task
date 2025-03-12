from rest_framework import serializers

from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):

    balance = serializers.SerializerMethodField()

    class Meta:
        model = Wallet
        fields = "__all__"
        read_only_fields = ["balance"]

    def get_balance(self, obj):
        return obj.balance
