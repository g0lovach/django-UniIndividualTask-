from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

from .models import Firms, Technic, Types
from .forms import FirmsForm
from django.http import HttpResponse

# Create your views here.

def index(request):
    firms = Firms.objects.all()
    types = Types.objects.all()
    technic = Technic.objects.all()
    return render(request, 'Main/index.html', {'title' : 'Главная', 'firms' : firms, 'types' : types, 'technic':technic})


def edit(request, id):
    try:
        firm = Firms.objects.get(id=id)
 
        if request.method == "POST":
            firm.firm_name = request.POST.get("firm_name")
            firm.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, "Main/edit.html", {"firm": firm})
    except Firms.DoesNotExist:
        return HttpResponseNotFound("<h2>Firm not found</h2>")

def edit_type(request, id):
    try:
        type = Types.objects.get(id=id)
 
        if request.method == "POST":
            type.type_name = request.POST.get("type_name")
            type.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, "Main/edit_type.html", {"type": type})
    except Types.DoesNotExist:
        return HttpResponseNotFound("<h2>Type not found</h2>")


def edit_technic(request, id):
    try:
        tech = Technic.objects.get(id=id)
        firms = Firms.objects.all()
        types = Types.objects.all()
 
        if request.method == "POST":
            tech.technic_name = request.POST.get("technic_name")
            firm_id = request.POST.get("firm")
            tech.firm = Firms.objects.get(pk=firm_id)
            type_id = request.POST.get("type")
            tech.type = Types.objects.get(pk=type_id)
            tech.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, "Main/edit_technic.html", {"technic": tech, "firms" : firms, "types" : types})
    except Technic.DoesNotExist:
        return HttpResponseNotFound("<h2>Technic not found</h2>")

def create_technic(request):
    firms = Firms.objects.all()
    types = Types.objects.all()
    technic = Technic.objects.all()
    if request.method == "POST":
        tech = Technic()
        tech.technic_id = technic.count() + 1
        tech.technic_name = request.POST.get("technic_name")
        firm_id = request.POST.get("firm")
        tech.firm = Firms.objects.get(pk=firm_id)
        type_id = request.POST.get("type")
        tech.type = Types.objects.get(pk=type_id)
        tech.save()
    else:
        return render(request, "Main/create_technic.html", {"firms" : firms, "types" : types})
    return HttpResponseRedirect("/")