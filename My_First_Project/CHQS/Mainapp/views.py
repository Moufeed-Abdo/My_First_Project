from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models
from .forms import StudentForm, MemoForm

class IndexView(TemplateView):
    template_name = 'Mainapp_temp/index.html'

class StuListView(ListView):
    context_object_name = 'student_list'
    model = models.Student
    template_name = 'Mainapp_temp/stu_list.html'

#--------------------------------------------------

def Register(request):
    registered = False

    if request.method == 'POST':
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        student_form = StudentForm(data=request.POST)

        # Check to see both forms are valid
        if student_form.is_valid():

            # Save User Form to Database
            student = student_form.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(student_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        student_form = StudentForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request, 'Mainapp_temp/stu_reg.html', {'student_form': student_form,'registered': registered})

#--------------------------------------------------

def Record(request):
    registered = False

    if request.method == 'POST':
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        record_form = MemoForm(data=request.POST)

        # Check to see both forms are valid
        if record_form.is_valid():

            # Save User Form to Database
            record = record_form.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(record_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        record_form = MemoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request, 'Mainapp_temp/record.html', {'record_form': record_form,'registered': registered})