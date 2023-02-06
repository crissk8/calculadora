from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def suma(num1,num2):
    result = int(num1) + int(num2)
    return result

def resta(num1,num2):
    result=int(num1) - int(num2)
    return result 

def division(num1,num2):
    result=int(num1)/int(num2)
    return result 

def multiplicacion(num1,num2):
    result=int(num1)*int(num2)
    return result 
def home(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        if 'sum' in request.POST:
            result = Suma(num1,num2)
            return render(request,'index.html',{'result':result})

        if 'res' in request.POST:
            result = resta(num1,num2)
            return render (request,'index.html',{'result':result})

        if 'div' in request.POST:
            result = division(num1,num2)
            return render (request,'index.html',{'result':result})

        if 'mul' in request.POST:
            result = multiplicacion(num1,num2)
            return render (request,'index.html',{'result':result})
    return render(request,'index.html')
