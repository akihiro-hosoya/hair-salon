from django import forms
from allauth.account.forms import SignupForm
from app.models import User, Staff
from .models import CustomUser


class SignupUserForm(SignupForm):
    name = forms.CharField(max_length=50, label='名前')
    furigana = forms.CharField(max_length=50, label='フリガナ')
    address = forms.CharField(max_length=100, label='住所')
    tel = forms.CharField(max_length=100, label='電話番号')

    def save(self, request):
        user = super(SignupUserForm, self).save(request)
        user_profile = User()
        user_profile.account_core = CustomUser.objects.filter(email=self.cleaned_data['email'])[0]
        user_profile.name = self.cleaned_data['name']
        user_profile.furigana = self.cleaned_data['furigana']
        user_profile.address = self.cleaned_data['address']
        user_profile.tel= self.cleaned_data['tel']
        user_profile.save()
        return user

class SignupStaffForm(SignupForm):
    name = forms.CharField(max_length=50, label='名前')
    furigana = forms.CharField(max_length=50, label='フリガナ')
    position = forms.CharField(max_length=50, label='役職')
    address = forms.CharField(max_length=100, label='住所')
    tel = forms.CharField(max_length=100, label='電話番号')

    def save(self, request):
        user = super(SignupStaffForm, self).save(request)
        staff = Staff()
        staff.account_core = CustomUser.objects.filter(email=self.cleaned_data['email'])[0]
        staff.name = self.cleaned_data['name']
        staff.furigana = self.cleaned_data['furigana']
        staff.position = self.cleaned_data['position']
        staff.address = self.cleaned_data['address']
        staff.tel = self.cleaned_data['tel']
        staff.save()
        return user

class ProfileUserForm(forms.Form):
    name = forms.CharField(max_length=30, label='名前')
    furigana = forms.CharField(max_length=30, label='フリガナ')
    address = forms.CharField(max_length=100, label='住所')
    tel = forms.CharField(max_length=100, label='電話番号')

class ProfileStaffForm(forms.Form):
    name = forms.CharField(max_length=30, label='名前')
    furigana = forms.CharField(max_length=30, label='フリガナ')
    description = forms.CharField(label='自己紹介', widget=forms.Textarea(), required=False)
    address = forms.CharField(max_length=100, label='住所')
    tel = forms.CharField(max_length=100, label='電話番号')