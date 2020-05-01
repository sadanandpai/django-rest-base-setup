from django.contrib.auth.models import User
from rest_framework import serializers
from portal.models import Fish


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'groups']

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = [
            'url',
            'Userid',
            'fishid',
            'size',
            'price',
            'status',
            'created_date',
            'modified_date',
        ]
        