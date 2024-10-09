from rest_framework import serializers
from .models import User,Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','password','is_email_verified','otp')
        extra_kwargs = {"password":{"write_only":True}}     # we don't want to return the password while return the user in the api response

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','user','content','is_completed','created_at')
