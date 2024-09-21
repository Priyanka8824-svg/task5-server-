from rest_framework import serializers
from task_app.serializers import TaskSerialzier
from django.contrib.auth import get_user_model
User = get_user_model()

class UserTasksSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format="%d/%m/%y %H:%M:%S", read_only=True) 
    assigner = TaskSerialzier(many=True, read_only=True)
    assignee = TaskSerialzier(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ['id', 'date_joined', 'last_login', 'groups', 'user_permissions', 'assigner', 'assignee']

class UserDetailSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format="%d/%m/%y %H:%M:%S", read_only=True)
    last_login = serializers.DateTimeField(format="%d/%m/%y %H:%M:%S", read_only=True)

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ['id', 'date_joined', 'last_login', 'groups', 'user_permissions']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, instance, valdiated_data):
        instance.email = valdiated_data.get('email', instance.email)
        instance.gender = valdiated_data.get('gender', instance.gender)
        instance.address = valdiated_data.get('address', instance.address)
        instance.pincode = valdiated_data.get('pincode', instance.pincode)
        instance.city = valdiated_data.get('city', instance.city)
        instance.contact = valdiated_data.get('contact', instance.contact)
        instance.role = valdiated_data.get('role', instance.role)
        instance.profile_pic = valdiated_data.get('profile_pic', instance.profile_pic)
        instance.company = valdiated_data.get('company', instance.company)
        instance.save()
        return instance