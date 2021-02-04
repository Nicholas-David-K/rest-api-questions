from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.conf import settings
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.utils.encoding import force_text
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode as uid_decoder

class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('id','first_name', 'last_name', 'email', 'gender', 'age', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)




from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password_reset_form_class = PasswordResetForm

    def validate_email(self, value):
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError('error')

        
        if not get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError('This is an invalid email')
        return value
    
    def save(self):
        request = self.context.get('request')
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            
            'email_template_name': 'example_message.txt',
            'request': request
        }

        self.reset_form.save(**opts)