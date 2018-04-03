from django.shortcuts import render
from .models import UserMessage


# Create your views here.

def get_form(request):
    message = None
    all_message = UserMessage.objects.filter(name='test')
    if all_message:
        message = all_message[0]
    if request.method == 'POST':
        name = request.POST.get('name', '')
        message = request.POST.get('name', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')
        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.save()
    return render(request, 'message_form.html', {'my_message': message})
