from rest_framework import serializers

from index.models import Subscriber



class SubscriberSerializer(serializers.HyperlinkedModelSerializer):

    def validate_email(self, value):
        if Subscriber.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError("This email already exists.")
        return value.lower()

    class Meta:
        model = Subscriber
        fields = ('email',)