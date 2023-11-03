from django.shortcuts import render, redirect
from .forms import contactForm
from .models import Contact
def contact_us(request):
    form =contactForm()
    if request.method == 'POST':
        # Assuming you have a form with fields 'name', 'email', and 'message'
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Do something with the form data, e.g., send an email, save to database, etc.
        obj = Contact(name=name, email=email, message=message)
        obj.save()
        return render(request, 'submissions.html', {'name': name, 'email': email, 'message': message})
    else:
        return render(request, 'contactUs.html', {"form": form})


# def contact_us(request):
#     if request.method=='POST':
#         form=contactForm(request.POST)
#         if form.is_valid():
#             name=form.cleaned_data['name']
#             email=form.cleaned_data['email']
#             message=form.cleaned_data['message']
#             return redirect('submissions',name=name, email=email, message=message)
#

    # else:
    #     form=contactForm()
    # return render(request, 'submissions.html', {'name':name, 'email':email, 'message':message})

def submissions(request):
    # Your view logic goes here
    return render(request, 'submissions.html')

