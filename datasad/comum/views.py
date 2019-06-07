from django.shortcuts import render

def index(request):
    return render(request, 'datasad_index.html')