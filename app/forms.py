from django import forms
class StudentForm(forms.Form):
    sid=forms.IntegerField()
    sname=forms.CharField(max_length=100)
    semail=forms.EmailField()