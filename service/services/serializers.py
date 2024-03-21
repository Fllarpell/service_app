from rest_framework import serializers

from services.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.company_name', read_only=True)
    email = serializers.EmailField(source='client.user.email', read_only=True)

    class Meta:
        model = Subscription
        fields = ('id', 'plan_id', 'client_name', 'email')


