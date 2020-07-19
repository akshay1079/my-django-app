from django import forms

class StudentForm(forms.Form):
    rn = forms.IntegerField(label="Enter Your Roll No.")
    marks = forms.FloatField(label="Enter Your Marks ")
    email = forms.EmailField(label="Enter Email..")
    name = forms.CharField(label="Enter Your Name" ,max_length=30)
    file = forms.FileField(label="Put Your Resume Here..")