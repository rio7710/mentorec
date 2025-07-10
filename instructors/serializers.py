# instructors/serializers.py

from rest_framework import serializers
from .models import InstructorProfile

class InstructorProfileSerializer(serializers.ModelSerializer):
    # User 모델의 username을 보여주기 위함
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = InstructorProfile
        fields = ['user', 'username', 'bio', 'expertise', 'years_of_experience']
        read_only_fields = ['user', 'username']