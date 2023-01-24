from django.shortcuts import render
import datetime
# Create your views here.

def index(request):
    ahora =datetime.datetime.now()
    return render (request, "aniversario/index.html", {
            "Aniversario": ahora.month == 6 and ahora.day == 27})
