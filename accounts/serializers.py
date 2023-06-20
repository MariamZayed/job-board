from rest_framework import serializers 
from  django.contrib.auth.models import User
from .models import Profile, City


class UserSerializer(serializers.ModelSerializer):
    print("hello world")
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
    
    # checking if passwords are same
    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 != password2:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    
    # hasing password
    def create(self, validated_data):# The create method has been overridden to handle setting the password for the user 
        password = validated_data.pop('password1') # all the valited data is on validated_data dictionary
        validated_data.pop('password2') 
        user = User(**validated_data) #A new User instance is created using the remaining fields in the validated_data dictionary: user = User(**validated_data). This initializes the user object with the provided data.
        user.set_password(password) # handles the password hashing,
        user.save()
        return user
    
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer() # nested serializers for the user and city
    city = CitySerializer() # So when you serialize a Profile instance, the serialized data will also include the serialized City and user

    class Meta:
        model = Profile
        fields = ['user','phone_number', 'image', 'city']