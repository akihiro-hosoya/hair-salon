from django import forms
from .models import CustomUser
from app.models import User, Staff

# class MenuChoiceForm(forms.Form):
    # カット
    # カラー


class BookingForm(forms.Form):
    name = forms.CharField(max_length=30, label='名前')
    furigana = forms.CharField(max_length=30, label='フリガナ')
    tel = forms.CharField(max_length=30, label='電話番号')
    address = forms.CharField(max_length=100, label='住所')
    remarks = forms.CharField(label='備考', widget=forms.Textarea(), required=False)