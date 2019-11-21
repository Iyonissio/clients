from django.http import HttpResponse
from django.shortcuts import render


def do_calculation(valor1,valor2):
    return valor1*valor2

def test(request):
    tot=do_calculation(2,4)
    p_fla=True
    people = ['Alfredo','Ansha','Marriamo','Antonio','Jose']
    return render(request,'example.html',{'total': tot, 'people':people, 'p_fla':p_fla})


#def list_clients(request):
#   return HttpResponse('Hello Mundo')