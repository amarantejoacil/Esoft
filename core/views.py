from django.shortcuts import render, redirect
from core.models import Endereco
from core.forms import EnderecoForms

# Create your views here.

def consultaCep(request):
    pass
    # if request.method == 'POST':

def IndexView(request):
    obj_endereco = Endereco.objects.all()
    context = {
        'obj_endereco':obj_endereco
    }

    return render(request, 'consulta.html', context)


def CadastrarEndereco(request):
    form = EnderecoForms()
    if request.method == 'POST':
        form = EnderecoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'cadastro.html', context)


# def AtualizarEndereco(request, pk):
#     endereco = Endereco.objects.get(id=pk)
#     form = EnderecoForms(instance=endereco)
#
#     if request.method == 'POST':
#         form = EnderecoForms(request.POST, instance=endereco)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     context = {
#         'form': form
#     }
#
#     return redirect(request, 'cadastro.html', context)


def DeletarEndereco(request, pk):
    endereco = Endereco.objects.get(id=pk)
    if request.method == 'POST':
        endereco.delete()
        return redirect('index')

    context = {'endereco':endereco}
    return render(request, 'delete.html', context)
