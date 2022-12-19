from django.http import HttpResponse
from django.shortcuts import render
from .models import Dht

def dht11(request):
    return render(request, 'index.html')
def dht112(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'index2.html', s)
# Create your views here.
def dht113(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'index3.html', s)
def jour1(request):
    jr1 = Dht.objects.all()[:12]
    s1 = {'jr1': jr1}
    return render(request, 'jour1.html', s1)
def jour2(request):
    jr2 = Dht.objects.all()[:5]
    s2 = {'jr2': jr2}
    return render(request, 'jour2.html', s2)
def jour3(request):
    jr3= Dht.objects.all()[:3]
    s3 = {'jr3': jr3}
    return render(request, 'jour3.html', s3)
def Gjour1(request):
    jr1= Dht.objects.all()[:3]
    s1 = {'jr1': jr1}
    return render(request, 'Gjour1.html', s1)
def Gjour2(request):
    jr2= Dht.objects.all()[:3]
    s2 = {'jr2': jr2}
    return render(request, 'Gjour2.html', s2)
def Gjour3(request):
    jr3= Dht.objects.all()[:3]
    print("jre 3 :", jr3)
    s3 = {'jr3': jr3}
    return render(request, 'Gjour3.html', s3)
def historique(request):
    return render(request, 'historique.html')


