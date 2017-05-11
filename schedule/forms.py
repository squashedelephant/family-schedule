from django import forms

from schedule.models import Child, Dashboard, Event, Parent

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'parents']

class DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ['child', 'parents', 'weekday']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['child', 'parent', 'created', 'name', 'color', 'count']

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent 
        fields = ['first_name', 'last_name']

