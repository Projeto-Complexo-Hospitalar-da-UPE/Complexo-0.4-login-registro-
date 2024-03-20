from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ExamesForm

# Create your views here.
def cliente_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Login nao encontrado, tente novamente"))
            return redirect('login_cliente:cliente_login')

    else:
        return render(request, 'pagina_login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request, ("Voce saiu da sua conta"))
    return redirect('home')

def registro_exames(request):
    submitted = False
    if request.method == "POST":
        form = ExamesForm(request.POST, request.FILES)
        if form.is_valid():
            """
            paciente = form.cleaned_data['paciente']
            nome_exame = form.cleaned_data['nome_exame']
            data_realizacao = form.cleaned_data['data_realizacao']
            descricao = form.cleaned_data['descricao']
            concluido = form.cleaned_data['concluido']
            arquivo = form.cleaned_data['arquivo']
            p = ExamesForm(paciente=paciente, nome_exame=nome_exame, data_realizacao=data_realizacao, descricao=descricao, concluido=concluido, arquivo=arquivo)
            p.save()
            """
            form.save()
            submitted=True
        else:
            form = ExamesForm()
            #messages.success(request, ("Registro nao valido, tente novamente"))
            if 'submitted' in request.GET:
                submitted = True

    form = ExamesForm
    return render(request, 'registro_exames.html', {'form' : ExamesForm, 'submitted':submitted})


