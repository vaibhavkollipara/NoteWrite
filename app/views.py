from django.http import HttpResponse

# Create your views here.


def indexView(request):
    return HttpResponse("Hello")
