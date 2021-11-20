from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Users, Groups


# Create your forms here.

class RegisterUser(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterUser, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            group = Groups.objects.get(description__exact="Leitor")
            u = Users(first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name'], username=self.cleaned_data['username'], group=group, favourites=blank)
            u.save()
        return user


class SearchPubForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200, required=False)
    date = forms.DateField(label="Date", required=False, widget=forms.widgets.DateInput(attrs={'type': 'date','class': 'datetimepicker-input','data-target': '#datetimepicker1'}))

