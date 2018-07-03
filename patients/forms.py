from django import forms
from django.contrib.auth.models import User
from patients.models import ( Checklist,Checklistitems,Profile, Insurance,
                            Biometric)

MY_CHOICES = (
    ('u', 'Underweight'),
    ('n', 'Normal'),
    ('o', 'Overweight'),
    ('x', 'Obesity I'),
    ('y', 'Obesity II'),
    ('z', 'Obesity III'),
)
# class ChecklistForm(forms.Form):
#     Patient = forms.SelectMultiple()
#     Check_off = forms.MultipleChoiceField(required=False,
#                             widget=forms.CheckboxSelectMultiple, choices=MY_CHOICES)
# class InfoForm(forms.ModelForm):
#     class Meta:
#         model = Info
#         fields = ['date_of_birth']
#         widgets = {
#             'date_of_birth': forms.DateTimeInput(attrs={'class': 'datetime-input'})
#         }
#
#
# class InfosForm(forms.ModelForm):
#     class Meta:
#         model = Info
#         widgets = {'date_of_birth': forms.DateInput(attrs={'class':'datepicker'})}
#         fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class ProfileForm(forms.ModelForm):

    class Meta():
        model = Profile
        exclude = ['user']
        # fields = ('first_name','last_name', 'middle_name', 'preferred_name',
        #             'date_of_birth','gender','ethnicity','height','program','phone','insurance',
        #             'initial','profile_pic','notes','address1','address2',
        #             'state','country','branch','date_join','appointment')

class BiometricForm(forms.ModelForm):

    class Meta():
        model = Biometric
        fields = ('user','height','weight')
