from django.shortcuts import render


# Create your views here.

def get_form(request):
    return render(request, 'message_form.html')
