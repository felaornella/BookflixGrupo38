from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User
class UserCreationFormExtends(UserCreationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto
    email = forms.EmailField(label="Correo electrónico")
    first_name= forms.CharField(label="Nombre")
    last_name= forms.CharField(label="Apellido")
    dni= forms.CharField(label='DNI')
    nacimiento= forms.DateField(label='Fecha de Nacimiento')




    class Meta:
        model = User
        fields = ["username", "password1", "password2","email","first_name","last_name","dni","nacimiento"]