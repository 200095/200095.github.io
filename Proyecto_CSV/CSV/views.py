from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, "CSV/index.html")

def conocer(request):
    return render(request, "CSV/Conocenos.html")

def inicio(request):
    return render(request, "CSV/index.html")

def contactar(request):
    return render(request, "CSV/Contacto.html")

def iniciar(request):
    return render(request, "CSV/InicioDeSesion.html")

def soporte(request):
    return render(request, "CSV/Soporte_Remoto.html")

class FormularioCSV (forms.Form):
        csv = forms.CharField(label="Nueva CSV", widget=forms.TextInput(attrs={'placeholder': 'Nuevo usuario'}))


def add(request):
        #request.session["usuario"] = [] 
        #Linea para eliminar
        if "usuario" not in request.session:
                request.session["usuario"] = []
        return render(request, "CSV/add.html", {
            "usuarios": request.session["usuario"] ,
        })

def login(request):
        print(request.POST["usuario"])
        print(request.POST)
        usuario = request.POST["usuario"]
        return render(request, "CSV/index.html", {"usuario" : usuario})

def iniciar(request):
        if request.method == "POST":
                formulario = FormularioCSV(request.POST)
                if formulario.is_valid():
                        usuario = formulario.cleaned_data.get("csv").upper()
                        print(request.session["usuario"])
                        print(usuario)
                        if usuario not in request.session["usuario"]:
                                request.session["usuario"] += [usuario]
                                return HttpResponseRedirect(reverse("CSV:add"))
                        else:   
                                return render(request, "CSV/InicioDeSesion.html", {
                                        "form": formulario, "msg" : "El usuario ya está registrado."
                                })
                else:   
                        return render(request, "CSV/InicioDeSesion.html", {
                                "form": formulario
                        })
        else:
                return render(request, "CSV/InicioDeSesion.html", {
                        "form":FormularioCSV()
                })