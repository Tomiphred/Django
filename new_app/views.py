from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the New Django Project Home Page!")
