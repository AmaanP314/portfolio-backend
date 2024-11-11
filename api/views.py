# # # api/views.py

# # from rest_framework import viewsets
# # from .models import Project, BlogPost
# # from .serializers import ProjectSerializer, BlogPostSerializer

# # class ProjectViewSet(viewsets.ModelViewSet):
# #     queryset = Project.objects.all()
# #     serializer_class = ProjectSerializer

# # class BlogPostViewSet(viewsets.ModelViewSet):
# #     queryset = BlogPost.objects.all()
# #     serializer_class = BlogPostSerializer

# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework import status

# # class HelloWorldView(APIView):
# #     def get(self, request):
# #         return Response({"message": "Hello, World!"}, status=status.HTTP_200_OK)

# from django.core.mail import send_mail
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['POST'])
# def send_email(request):
#     name = request.data.get('name')
#     email = request.data.get('email')
#     message = request.data.get('message')

#     if name and email and message:
#         # Compose the email content
#         subject = f"Portfolio Contact Form Submission from {name}"
#         email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

#         # Send the email
#         send_mail(
#             subject,
#             email_message,
#             'amaanpoonawala05@gmail.com',  # Replace with your email
#             ['amaanhannan0@gmail.com'],  # Replace with the recipient's email
#             fail_silently=False,
#         )
#         return Response({'message': 'Email sent successfully!'}, status=status.HTTP_200_OK)
#     else:
#         return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

@api_view(['POST'])
def send_email(request):
    if request.method == 'POST':
        name = request.data.get('name')
        user_email = request.data.get('email')
        message = request.data.get('message')

        if not name or not user_email or not message:
            return Response({"error": "All fields are required."}, status=400)

        # Format the email content
        email_subject = f"New Contact Form Submission from {name}"
        email_message = f"Name: {name}\nEmail: {user_email}\n\nMessage:\n{message}"

        # Send email to yourself (recipient)
        send_mail(
            subject=email_subject,
            message=email_message,
            from_email=user_email,  # The sender is the user's email
            recipient_list=[settings.EMAIL_HOST_USER],  # Your email (recipient)
            fail_silently=False,
        )

        return Response({"success": "Email sent successfully!"})
