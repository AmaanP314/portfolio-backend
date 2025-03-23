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

        email_subject = f"New Contact Form Submission from {name}"
        email_message = f"Name: {name}\nEmail: {user_email}\n\nMessage:\n{message}"

        send_mail(
            subject=email_subject,
            message=email_message,
            from_email=user_email,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return Response({"success": "Email sent successfully!"})

@api_view(['POST'])
def send_email_lab(request):
    name = request.data.get('fullName')  
    user_email = request.data.get('email')
    phone = request.data.get('phone')
    medicare_id = request.data.get('medicareId')

    if not name or not user_email or not phone or not medicare_id:
        return Response({"error": "All fields are required."}, status=400)

    email_subject = f"Contact Form Submission from {name}"
    email_message = f"Name: {name}\nEmail: {user_email}\nPhone: {phone}\nMedicare ID: {medicare_id}"

    send_mail(
        subject=email_subject,
        message=email_message,
        from_email=user_email,
        recipient_list=[os.getenv('EMAIL_HOST_USER') ],
        fail_silently=False,
    )
    return Response({"success": "Email sent successfully!"})

@api_view(['GET'])
def health_check(request):
    return Response({"status": "Server is awake!"}, status=200)
