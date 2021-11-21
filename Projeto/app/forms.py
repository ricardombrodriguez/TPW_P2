from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Users, Groups, Publication_topics


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
            u = Users(first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name'], username=self.cleaned_data['username'], group=group)
            u.save()
        return user

class SearchPubForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200, required=False)
    author = forms.CharField(label="Author", max_length=200, required=False)
    topic = forms.ModelChoiceField(queryset=Publication_topics.objects.all(),label="Topic",required=False)
    date = forms.DateField(label="Date", required=False, widget=forms.widgets.DateInput(attrs={'type': 'date','class': 'datetimepicker-input','data-target': '#datetimepicker1'}))


class AddPublication(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    content = forms.CharField(widget=forms.Textarea(attrs={"id":"summernote"}))
    categoria = forms.CharField(label="Categoria", max_length=200)


class AddComment(forms.Form):
    content =forms.CharField(widget=forms.Textarea(attrs={"id":"comment","cols":170,"onkeyup":"required1()",
                "rows": "5", "placeholder":"Escreva aqui o seu comentário..."}))
