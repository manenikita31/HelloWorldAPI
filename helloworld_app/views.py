# from django.shortcuts import render
# from django.http import JsonResponse
# def hello_world(request):
#     hello_messages = {
#         "English" : "Hello World",
#         "French" : "Bonjure le monde",
#         "Hindi" : "Namastey Sansar"
#     }
  
#     language = request.GET.get('language', 'English')
#     message = hello_messages.get(language , "Hello World")

#     return JsonResponse({"message" :message})

# def index(request):
#     return render(request, 'index.html')
# # Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import uuid  # To generate unique IDs for each message

def hello_world(request):
    # Define the available hello messages for different languages
    hello_messages = {
        "English": "Hello world",
        "French": "Bonjour le monde",
        "Hindi": "Namastey sansar"
    }
    
    # Get the language parameter from the query string
    language = request.GET.get('language')
    
    if language in hello_messages:
        # Generate a unique ID for the message
        message_id = str(uuid.uuid4())[:10]  # Generate a short, unique ID (first 10 characters)
        
        # Structure the response to match the MessageSummary schema
        return JsonResponse({
            "ID": message_id,
            "msgText": hello_messages[language]
        })
    else:
        # Return a 400 error response if the language is unsupported
        return JsonResponse({
            "error_message": "The requested language is not supported"
        }, status=400)
def index(request):
    return render(request, 'index.html')
