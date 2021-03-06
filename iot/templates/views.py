from django.shortcuts import render,redirect
from .models import iotdata,image

def first(request):
    
    return render(request,"first.html")

def second(request):
    t=request.POST["temp"]
    p=request.POST["pressure"]
    a=request.POST["alt"]
    roof=iotdata(temprature=t,pressure=p,altitude=a)
    roof.save()
    data=iotdata.objects.all()
    imag=image.objects.all()
    if int(t)>=0 and int(t)<=10 :
        con=15
        quote="It's too cold out side."
    elif int(t)>=11 and int(t)<=20:
        con=17
        quote="In the cold dark of winter,dream about the flower to get warmed up!"
    elif int(t)>=21 and int(t)<=25:
        con=10
        quote="Keep your face to the sun and you will never see the shadows."
    elif int(t)>=26 and int(t)<=29:
        con=8
        quote="Sunshine is the best medicine."
    elif int(t)>=30 and int(t)<=32:
        con=18
        quote="Get lost in nature and you will find yourself."
    elif int(t)>=33 and int(t)<=34:
        con=5
        quote="Spring work is going on with joyful enthusiasm."
    elif int(t)>=35 and int(t)<=36:
        con=13
        quote="Spring being a tough act to follow,God created june."
    elif int(t)>=37 and int(t)<=39:
        con=19
        quote="Fact:Extreme heat can cause cramps,swelling and fainting."
    elif int(t)>=40:
        con=14
        quote="It's too hot outside."


    return render(request,"second.html",{'t':t,'m':imag,'c':con,'p':p,'a':a,'q':quote})

def live(request):
    data=iotdata.objects.all()
    return render(request,"live.html",{'data':data})

def temp(request):
    data=iotdata.objects.all()
    
    return render(request,"tempgraph.html",{'data':data})

def presslive(request):
    data=iotdata.objects.all()
    
    return render(request,"livep.html",{'data':data})

def press(request):
    data=iotdata.objects.all()
    
    return render(request,"pregraph.html",{'data':data})

def alt(request):
    data=iotdata.objects.all()
    
    return render(request,"altgraph.html",{'data':data})

def all(request):
    data=iotdata.objects.all()
    
    return render(request,"all.html",{'data':data})