from django.http import HttpResponse
from .task import print_hello
# Create your views here.

def hello(request):
    print_hello.delay()
    return HttpResponse("Give me 3 seconds")
