from django import forms
from .models import Student,Tracing


from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('user','name','admnno','designation','sclass','age','phone','health','remarks')

    def __init__(self, user, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['name'].queryset = User.objects.filter(username=user)

class TracingForm(forms.ModelForm):

    class Meta:
        model = Tracing
        fields = ('user','status')

    def __init__(self, user, *args, **kwargs):
        super(TracingForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(username=user)