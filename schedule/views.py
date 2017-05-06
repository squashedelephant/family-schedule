from django.http import HttpResponse
from django.shortcuts import redirect, render

from schedule.constant import Constant
from schedule.error import Error
from schedule.forms import ChildForm, DashboardForm, EventForm, ParentForm
from schedule.message import Message
from schedule.models import Child, ChildImage, Event, Parent, ParentImage

def redirect(request):
    destination = '/index'
    return redirect(destination)

def home(request):
    """
    load default webpage
    """
    if not request.method == 'GET':
        return Error.http405()
    context = {}
    context['title'] = Constant.TITLE
    context['header'] = Constant.HEADER
    context['footer'] = Constant.FOOTER
    html = render(request, 'base.htm', context)
    return HttpResponse(html)

def create_dashboard(request):
    if request.method not in ['POST', 'GET']:
        return Error.http405()
    elif request.method == 'GET':
        form = DashboardForm()
        return render(request, 'dashboard.htm', {'form': form})
    elif request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            return Error.debug(str(form.cleaned_data))
            try:
                p = Parent(first_name=form.cleaned_data['first_name'],
                           last_name=form.cleaned_data['last_name'])
                p.save()
                return Message.object_created(p.id)
            except Exception as e:
                return Error.debug(str(e))

def create_parent(request):
    if request.method not in ['POST', 'GET']:
        return Error.http405()
    elif request.method == 'GET':
        form = ParentForm()
        return render(request, 'parent.htm', {'form': form})
    elif request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            try:
                p = Parent(first_name=form.cleaned_data['first_name'],
                           last_name=form.cleaned_data['last_name'])
                p.save()
                return Message.object_created(p.id)
            except Exception as e:
                return Error.debug(str(e))

def create_child(request):
    if request.method not in ['POST', 'GET']:
        return Error.http405()
    elif request.method == 'GET':
        form = ChildForm()
        return render(request, 'child.htm', {'form': form})
    elif request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            try:
                c = Child(first_name=form.cleaned_data['first_name'],
                          last_name=form.cleaned_data['last_name'])
                c.save()
                parents = form.cleaned_data['parents']
                return Error.debug(str(parents))

                return Message.object_created(c.id)
            except Exception as e:
                return Error.debug(str(e))

def create_event(request):
    if request.method not in ['POST', 'GET']:
        return Error.http405()
    elif request.method == 'GET':
        form = EventForm()
        return render(request, 'event.htm', {'form': form})
    elif request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            try:
                e = Event(name=form.cleaned_data['name'],
                          color=form.cleaned_data['color'],
                          count=form.cleaned_data['count'],
                          created=datetime.now())
                e.save()
                return Message.object_created(e.id)
            except Exception as e:
                return Error.debug(str(e))
