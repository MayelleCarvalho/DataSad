from django.shortcuts import render

def index(request):
    return render(request, 'datasad_index.html')

def exibir_login(request):
    return render(request, 'datasad_login.html')

def exibir_cadastro_usuario(request):
    return render(request, 'datasad_cadastro_usuario.html')

def exibir_home(request):
    return render(request, 'datasad_home.html')

def exibir_questionario_detail(request):
    return render(request, 'datasad_questionario_detail.html')