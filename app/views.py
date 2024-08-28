from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'a':100,'b':10, 'c':200}
    return render(request,'conditional.html',context=d)

def loop(request):
    d={'name':'vyshu','mobile':[12345,23456]}
    return render(request,'loop.html',context=d)