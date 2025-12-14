from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from allauth.account.adapter import get_adapter
from django.contrib.auth.models import User

class CustomerRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    USER_TYPE_CHOICES = (
        ('candidate', 'Candidate'),
        ('employer', 'Employer'),
    )
    user_type = serializers.ChoiceField(choices=USER_TYPE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type')

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        # data['first_name'] = self.validated_data.get('first_name')
        # data['last_name'] = self.validated_data.get('last_name')
        data['user_type'] = self.validated_data.get('user_type')
        return data

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)

        # Save user type to related profile
        user_type = self.cleaned_data.get('user_type')
        if user_type == 'candidate':
            from candidates.models import CandidateProfile
            CandidateProfile.objects.create(user=user)
        elif user_type == 'employer':
            from employers.models import EmployerProfile
            EmployerProfile.objects.create(user=user)

        return user
