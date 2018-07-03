from django.shortcuts import render

from .models import  Biometric, Lab, Checklist, Initial, Profile, Week
from django.urls import reverse_lazy
# from .forms import ChecklistForm

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.contrib.auth.decorators import permission_required
# Create your views here.
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
# from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    num_patients=Profile.objects.all().count()
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    return render(request,'index.html',context={'num_patients':num_patients,'num_visits':num_visits},)
# def index(request):
#     """
#     View function for home page of site.
#     """
#     # Generate counts of some of the main objects
#     num_books=Book.objects.all().count()
#     num_instances=BookInstance.objects.all().count()
#     num_genres=Genre.objects.filter(name__icontains='fiction').count()
#     num_books_contain_word = Book.objects.filter(title__icontains='the').count()
#     # Available books (status = 'a')
#     num_instances_available=BookInstance.objects.filter(status__exact='a').count()
#     num_authors=Author.objects.count()  # The 'all()' is implied by default.
#
#     # Number of visits to this view, as counted in the session variable.
#     num_visits=request.session.get('num_visits', 0)
#     request.session['num_visits'] = num_visits+1
#
#     # Render the HTML template index.html with the data in the context variable
#     return render(
#         request,
#         'index.html',
#         context={'num_books':num_books,'num_instances':num_instances,'num_genres':num_genres,
#         'num_books_contain_word':num_books_contain_word,'num_instances_available':num_instances_available,
#         'num_authors':num_authors,'num_visits':num_visits},
#     )


# def checklist(request):
#     if request.method == 'POST':
#         form = ChecklistForm(request.POST)
#         if form.is_valid():
#             pass  # does nothing, just trigger the validation
#     else:
#         form = ChecklistForm()
#     return render(request, 'patients/checklist_form.html', {'form': form})
class ProfileListView(LoginRequiredMixin,generic.ListView):
    model = Profile
    ordering = ['first_name']
class ProfileUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Profile
    fields = '__all__'

class ProfileDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Profile
    success_url = reverse_lazy('patients:profile')

class ProfileDetailView(LoginRequiredMixin,generic.DetailView):
    model = Profile

class ProfileCreate(LoginRequiredMixin,generic.CreateView):
    model = Profile
    fields = '__all__'

# class InfoListView(LoginRequiredMixin,generic.ListView):
#     model = Info
#     paginate_by = 10
#
#     ordering = ['first_name']

# class InfoDetailView(LoginRequiredMixin,generic.DetailView):
#     model = Info
#
# class InfoCreate(generic.CreateView):
#     model = Info
#     fields = '__all__'

class ChecklistCreate(LoginRequiredMixin,generic.CreateView):
    model = Checklist
    fields = '__all__'

class ChecklistList(LoginRequiredMixin,generic.ListView):
    model = Checklist
    ordering = ['name']
class ChecklistDetailView(LoginRequiredMixin,generic.DetailView):
    model = Checklist
class ChecklistUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Checklist
    fields = '__all__'
class ChecklistDelete(LoginRequiredMixin,generic.DeleteView):
    model = Checklist
    success_url = reverse_lazy('patients:checklist')
class WeekListView(LoginRequiredMixin,generic.ListView):
    model = Week
    fields = '__all__'
class WeekCreateView(LoginRequiredMixin,generic.CreateView):
    model = Week
    fields = '__all__'
class WeekDetailView(LoginRequiredMixin,generic.DetailView):
    model = Week
class WeekUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Week
    fields = '__all__'
class WeekDelete(LoginRequiredMixin,generic.DeleteView):
    model = Week
    success_url = reverse_lazy('patients:week')

class InitialListView(LoginRequiredMixin,generic.ListView):
    model = Initial
    fields = '__all__'

class InitialDetailView(LoginRequiredMixin,generic.DetailView):
    model = Initial

class InitialUpdate(LoginRequiredMixin,generic.UpdateView):
    model = Initial
    fields = '__all__'

class InitialDelete(LoginRequiredMixin,generic.DeleteView):
    model = Initial
    success_url = reverse_lazy('patients:initial')

class InitialCreate(LoginRequiredMixin,generic.CreateView):
    model = Initial
    fields = '__all__'

class BiometricCreate(LoginRequiredMixin, generic.CreateView):
    model = Biometric
    fields = '__all__'

class BiometricListView(generic.ListView):
    model = Biometric
    template_name ='patients/biometric_list.html'

class BiometricDetailView(LoginRequiredMixin,generic.DetailView):
    model = Biometric

class BiometricUpdate(LoginRequiredMixin,generic.UpdateView):
    model = Biometric
    fields = '__all__'

class BiometricDelete(LoginRequiredMixin,generic.DeleteView):
    model = Biometric
    success_url = reverse_lazy('patients:biometric')

# from .forms import InfosForm, UserForm, ProfileForm
from .forms import UserForm, ProfileForm

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'patients/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})

# def register_user(request):
#     if request.method == 'POST':
#         form = InfosForm(request.POST)
#         # check if the form in valid
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#
#             return redirect('home')
#     else:
#         form = InfosForm()
#
#     return render(request,'patients/info_form.html',{'form':form})

from django.contrib.auth.decorators import permission_required, login_required
from django.db import transaction

@login_required
@transaction.atomic
def register_profile(request):
    if request.method == 'POST':
        # user_form = UserForm(request.POST, instance=request.user)
        # profile_form = ProfileForm(request.POST, instance=request.user.profile)
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            # messages.success(request, _('Your profile was successfully updated!'))
            # messages.success(request, 'Your profile was successfully updated!')
            # return redirect('settings:profile')
            return redirect('patients:profile')
        else:
            # messages.error(request, _('Please correct the error below.'))
            # messages.error(request, 'Please correct the error below.')
            print(user_form.errors,profile_form.errors)
    else:
         # user_form = UserForm(instance=request.user)
         # profile_form = ProfileForm(instance=request.user.profile)

        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'patients/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



# @login_required
# @transaction.atomic
# def create_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully saved!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })
