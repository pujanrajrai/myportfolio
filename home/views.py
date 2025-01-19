from django.shortcuts import render, redirect
from home.models import Education, ContactUs
# Create your views here.
from .forms import ContactUsForm, EductationForm
from django.contrib import messages


def home(request):
    myeducations = Education.objects.all()
    contactus_form = ContactUsForm()
    mydata = request.POST
    if request.method == "POST":
        contactus_form = ContactUsForm(request.POST)
        if contactus_form.is_valid():
            ContactUs.objects.create(
                name=mydata.get("name"),
                email=mydata.get("email"),
                subjects=mydata.get("subjects"),
                message=mydata.get("subjects"),
            )
            messages.success(request, 'Thank your for contacting us')
            return redirect("home:home")
    context = {
        "educations": myeducations,
        "contactus_form": contactus_form,
    }
    return render(request, 'home.html', context)


def education_create(request):
    educationform = EductationForm()
    if request.method == "POST":
        educationform = EductationForm(request.POST)
    if educationform.is_valid():
        educationform.save()
        print("data saved")
    context = {
        "educationform": educationform,
    }
    return render(request, 'create_education.html', context)
