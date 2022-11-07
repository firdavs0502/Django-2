from django.shortcuts import render

def asosiy(request):
    return render(request, 'index.html')



def qulpnaylar(request):
    return render(request, 'strawberry.html')

def olmalar(request):
    return render(request, 'apple.html')

def qovoqlar(request):
    return render(request, 'pumpkin.html')