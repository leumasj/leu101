from django.shortcuts import render


def index(request):
    return render(request, 'portf/index.html')



# Create your views here.
