from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Produto

# Create your views here.

def index(request):
    # print(dir(request))
    # print(f'User: {request.user}')

    # if str(request.user) == 'AnonymousUser':
    #     status = 'Usuário não logado'
    # else:
    #     status = 'Usuário logado'

    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'outro Django',
        # 'logado': status,
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    # print(f'ID: {id}')
    # produtos = Produto.objects.get(id=id)
    produtos = get_object_or_404(Produto, id=id)

    context = {
        'produto': produtos
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    # return render(request, '404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
