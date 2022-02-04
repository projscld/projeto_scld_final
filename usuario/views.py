from django.shortcuts import redirect, render
from .models import Usuario
from .forms import UsuarioForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def listar_usuarios(request):
  usuario = Usuario.objects.all()
  return render(request, 'usuario/listar_usuarios.html', {'usuario' : usuario})

@login_required()
def cadastrar_usuario(request):
  if request.method == 'POST':
    form = UsuarioForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('listar_usuarios')
  else:
    form = UsuarioForm()
  return render(request, 'usuario/form_usu.html', {'form': form})

def listar_usuario_id(request, id):
  user = Usuario.objects.get(id=id)
  return render(request, 'usuario/lista_usuario.html', {'user': user})

@login_required()
def editar_usuario(request, id):
  user = Usuario.objects.get(id=id)
  form = UsuarioForm(request.POST or None, instance=user)
  if form.is_valid():
    form.save()
    return redirect('listar_usuarios')
  return render(request, 'usuario/form_usu.html', {'form': form})

@login_required()
def remover_usuario(request, id):
  user = Usuario.objects.get(id=id)
  if request.method == 'POST':
    user.delete()
    return redirect('listar_usuarios')
  return render(request, 'usuario/confirma_exclusao.html', {'user': user}) 


def cadastrar_usu(request):
  if request.method == 'POST':
    form_usuario = UserCreationForm(request.POST)
    if form_usuario.is_valid():
      form_usuario.save()
      return redirect('listar_usuarios')
  else:
    form_usuario = UserCreationForm()
  return render(request, 'usuario/form_user.html', {'form_usuario': form_usuario})

def logar_usuario(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    usuario = authenticate(request, username=username, password=password)
    if usuario is not None:
      login(request, usuario)
      return redirect('listar_usuarios')
    else:
      messages.error(request, 'As credenciais estão incorretas')
      return redirect('logar_usuario')
  else:
    form_login = AuthenticationForm()
  return render(request, 'usuario/form_login.html', {'form_login': form_login})


def deslogar_usuario(request):
  logout(request)
  return redirect('logar_usuario')