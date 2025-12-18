from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email","first_name","last_name","contact_number","password1","password2"]

        # widgets = {
        #     "email":forms.EmailInput(attrs={"class":"form-control m-3","placeholder":"Enter email"}),
        #     "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter first name"}),
        #     "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter last name"}),
        #     "contact_number":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter contact number"})
           
        # }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        placeholders={
            "password1" : "create a strong password",
            "password2" : "confirm password",
            "email":"Enter email",
            "first_name":"enter first name",
            "last_name":"enter last name",
            "contact_number":"enter contact number"
        }
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':"form-control mb-3",
                'placeholder':placeholders.get(field,""),
                "required":"required"
                })



class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class':'form-control',
                                       'placeholder':'Enter registerd email',
                                       'required':'required'}
                                )
        )
    
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control',
                                          'placeholder':'Enter registerd password',
                                          'required':'required'}
                                   )
        )


class PasswordResetEmailForm(forms.Form):
    email = forms.EmailField(label="Enter your registered email")