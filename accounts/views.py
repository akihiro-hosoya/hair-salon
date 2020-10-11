from django.views import View
from accounts.forms import SignupUserForm, SignupStaffForm
from django.shortcuts import render, redirect
from allauth.account import views
from django.views.generic.edit import FormView

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