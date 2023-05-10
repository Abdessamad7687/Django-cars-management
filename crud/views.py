from django.shortcuts import render, redirect
from .models import Member,  Car
import datetime
from django.contrib import messages
from crud.forms import *
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):
    carstbl = Car.objects.all()
    return render(request, 'index.html', {'carstbl': carstbl})



def list(request):
    members_list = Member.objects.all()
    # members = Member.objects.all()
    paginator = Paginator(members_list, 5)
    page = request.GET.get('page')
    try:
        members = paginator.page(page)
    except PageNotAnInteger:  
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)
    return render(request, 'list.html', {'members': members_list})

# @login_required
def create(request):
    if request.method == 'POST':
        member = Member(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            mobile_number=request.POST['mobile_number'],
            description=request.POST['description'],
            location=request.POST['location'],
            date=request.POST['date'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            member.full_clean()
        except ValidationError as e:
            pass
        member.save()
        messages.success(request, 'Member was created successfully!')
        return redirect('/list')
    else:
        return render(request, 'add.html')

# @login_required
def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'edit.html', context)


# @login_required
def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.mobile_number = request.POST['mobile_number']
    member.description = request.POST['description']
    member.location = request.POST['location']
    member.date = request.POST['date']
    member.save()
    messages.success(request, 'Member was updated successfully!')
    return redirect('/list')

# @login_required
def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    messages.warning(request, 'Member was deleted successfully!')
    return redirect('/list')
