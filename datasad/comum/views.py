from django.shortcuts import render

def index(request):
    return render(request, 'datasad_index.html')

def exibir_login(request):
    return render(request, 'datasad_login.html')

def exibir_cadastro_usuario(request):
    return render(request, 'datasad_cadastro_usuario.html')

def exibir_questionario_list(request):
    return render(request, 'datasad_questionario_list.html')

def exibir_questionario_detail(request):
    return render(request, 'datasad_questionario_detail.html')

def exibir_cadastro_profissional(request):
    return render(request, 'datasad_cadastro_profissional.html')

def exibir_cadastro_aluno(request):
    return render(request, 'datasad_cadastro_aluno.html')

def exibir_cadastro_geral(request):
    return render(request, 'datasad_cadastro_geral.html')

def exibir_home(request):
    return render(request, 'datasad_home.html')

def exibir_tcle(request):
    return render(request, 'datasad_form_tcle.html')

def exibir_questionario(request):
    return render(request, 'datasad_questionario.html')

def exibir_cadastro_questionario(request):
    return render(request, 'datasad_cadastro_questionario.html')


def exibir_gerenciamento_permissoes(request):
    return render(request, 'datasad_gerenciar_permissoes.html')