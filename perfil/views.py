from django.shortcuts import render

def perfil(request):
    if request.method == "GET":
        return render(request, 'home.html')