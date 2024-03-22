from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes ,force_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import send_mail
from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PasswordResetSerializer, RegisterSerializer, PasswordSerializer
from rest_framework.permissions import AllowAny


class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer


class PasswordResetRequestAPIView(generics.CreateAPIView):
    serializer_class =PasswordResetSerializer
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            reset_url = f'http://127.0.0.1:8000/api/password-reset/confirm/{uid}/{token}/'
            send_mail(
                'Password Reset Request',
                f'Please click the following link to reset your password: {reset_url}',
                'admin.stylist@gmail.com',
                [email],
                fail_silently=False,
            )
            return Response({'success': 'Password reset email has been sent.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PasswordResetValidateAPIView(generics.ListCreateAPIView):
    serializer_class=PasswordSerializer
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):            
            return Response({'uidb64': uidb64, 'token': token, 'user':user.username}, status=status.HTTP_200_OK)
        else:
            return Response({"data":'Invalid password reset link.'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def post(self, request, uidb64, token):
        try:    
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({"data":'Invalid password reset link.'}, status=status.HTTP_401_UNAUTHORIZED)
        pwd=request.data.get('pwd')
        pwd2=request.data.get('pwd2')
        print(request.data)
        if user is not None and default_token_generator.check_token(user, token) and pwd==pwd2:
            user.set_password(pwd)
            user.save()
            return Response({'data': 'success password reset successfully.'}, status=status.HTTP_200_OK)
        
        return Response("Error: The Link is broken or has been used", status=status.HTTP_401_UNAUTHORIZED)