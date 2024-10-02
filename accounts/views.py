from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views import View
from django.conf import settings

class SignUpView(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char in '!@#$%^&*()' for char in password):
            return JsonResponse({'error': 'Password must be at least 8 characters long and include numbers and symbols.'}, status=400)
        user = User.objects.create_user(username=email, email=email, password=password)
        user.is_active = False
        user.save()
        send_verification_email(user.email)
        return JsonResponse({'message': 'Please confirm your email address to complete the registration.'}, status=200)