from django.views import View
from accounts.forms import SignupUserForm, SignupStaffForm, ProfileUserForm, ProfileStaffForm
from django.shortcuts import render, redirect
from allauth.account import views
from django.views.generic.edit import FormView
from app.models import Staff, User
from accounts.models import CustomUser

class SignupView(views.SignupView):
    template_name = 'accounts/signup.html'
    form_class = SignupUserForm

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        return context

class StaffSignupView(views.SignupView):
    template_name = 'accounts/staff_signup.html'
    form_class = SignupStaffForm

    def dispatch(self, request, *args, **kwargs):
        response = super(FormView, self).dispatch(request, *args, **kwargs)
        return response

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('/')
        form = SignupStaffForm(request.POST or None)
        return render(request, 'accounts/staff_signup.html', {
            'form': form
        })

class LoginView(views.LoginView):
    template_name = 'accounts/login.html'

class LogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        if request.user.account_type == 1:
            user_data = User.objects.get(account_core_id=request.user.id)

            return render(request, 'accounts/profile.html', {
                'user_data': user_data,
            })

        else:
            staff_data = Staff.objects.get(account_core_id=request.user.id)

            return render(request, 'accounts/profile.html', {
                'staff_data': staff_data,
            })

class ProfileEditView(View):
    def get(self, request, *args, **kwargs):
        if request.user.account_type == 1:
            user_data = User.objects.get(account_core_id=request.user.id)
            form = ProfileUserForm(
                request.POST or None,
                initial={
                    'name': user_data.name,
                    'furigana': user_data.furigana,
                    'address': user_data.address,
                    'tel': user_data.tel,
                }
            )
        
        else:
            staff_data = Staff.objects.get(account_core_id=request.user.id)
            form = ProfileStaffForm(
                request.POST or None,
                initial={
                    'name': staff_data.name,
                    'furigana': staff_data.furigana,
                    'description': staff_data.description,
                    'address': staff_data.address,
                    'tel': staff_data.tel,
                }
            )

        return render(request, 'accounts/profile_edit.html', {
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        if request.user.account_type == 1:
            form = ProfileUserForm(request.POST or None)
            if form.is_valid():
                user_data = User.objects.get(account_core_id=request.user.id)
                user_data.name = form.cleaned_data['name']
                user_data.furigana = form.cleaned_data['furigana']
                user_data.address = form.cleaned_data['address']
                user_data.tel = form.cleaned_data['tel']
                user_data.save()
                return redirect('profile')

        else:
            print(1)
            form = ProfileStaffForm(request.POST or None)
            if form.is_valid():
                staff_data = Staff.objects.get(account_core_id=request.user.id)
                staff_data.name = form.cleaned_data['name']
                staff_data.furigana = form.cleaned_data['furigana']
                staff_data.description = form.cleaned_data['description']
                staff_data.address = form.cleaned_data['address']
                staff_data.tel = form.cleaned_data['tel']
                staff_data.save()
                return redirect('profile')

        return render(request, 'accounts/profile.html', {
            'form': form
        })