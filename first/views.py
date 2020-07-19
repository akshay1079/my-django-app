from django.shortcuts import render
from django.http import HttpResponse
from .functions.functions import handle_uploaded_file
from .forms import StudentForm
import csv
# Create your views here.

def index1(request):
    template_name = 'first/index.html'

    context = {'a':[1,2,4,5,7,8,4]}
    return render(request,template_name,context)

def student(request):
    a = StudentForm()
    template_name = 'first/index.html'
    context = {'a':a}
    return render(request,template_name,context)


def index(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded Successfuly...")
    else:
        student = StudentForm()
        return render(request,"first/index.html",{'a':student})


def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename = "file.csv"'
    writer = csv.writer(response)
    writer.writerow(['1001','john','domil','CA'])
    writer.writerow(['1002','Amit','Mukharji','LA','"Testing"'])
    return response