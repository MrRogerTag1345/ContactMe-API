from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.http import JsonResponse
from backend.settings import *

@api_view(['GET', 'POST'])
def send_message(request):
    if request.method == 'GET':
        # Return a message or documentation about the API endpoint
        return JsonResponse({"message": "Send a POST request with name, email, and content to send a message."}, status=200)
    
    if request.method == 'POST':
        try:
            # Parse the JSON body of the POST request
            data = request.data  # Django Rest Framework automatically parses JSON body
            name = data.get('name', 'Unknown')
            email = data.get('email', 'No email provided')
            content = data.get('content', 'No content provided')
            if not name or not email or not content:
                return JsonResponse({"error": "Missing required fields."}, status=400)
            # Construct the email message
            subject = f"New Contact Message from {name}"
            message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{content}"
            from_email = email
            recipient_list = ["Chetaspatel1345@gmail.com"]
            # Send the email (no recipients specified)
            send_mail(subject, 
                    message, 
                    from_email, 
                    recipient_list,
                    fail_silently=False,
                    auth_user=EMAIL_HOST_USER,
                    auth_password=EMAIL_HOST_PASSWORD,
                    connection=None)
            # Return a response indicating the email was processed
            return JsonResponse({"message": "Email processed 1 recipients)."}, status=200)
        
        except Exception as e:
            # Return an error response if something goes wrong
            return JsonResponse({"error": str(e)}, status=500)
    
    # If the method is neither GET nor POST, return 405 Method Not Allowed
    return JsonResponse({"error": "Method not allowed"}, status=405)