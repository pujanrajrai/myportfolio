from django.shortcuts import render
from home.models import Education
# Create your views here.


def home(request):
    myeducations = Education.objects.all()
    context = {
        "educations": myeducations
    }
    return render(request, 'home.html', context)
