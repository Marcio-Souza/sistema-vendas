from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect


def home(request):
    try:
        messages.add_message(request, messages.SUCCESS, 'Seja bem vindo ao WEB VENDAS...')
        return render(request, 'home/home.html')
    except:
        messages.add_message(request, messages.ERROR, 'A página solicitada não existe...')
        return HttpResponseRedirect(request.META('HTTP_REFERER'))
    # message = 'Hello world'
    # return render(request, 'home/home.html', {'message': message})
