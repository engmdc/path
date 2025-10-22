from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import HallForm, FacilityForm, EventTypeForm
from .models import Hall, Facility, EventType

@login_required
def new_hall_creation(request):
    if request.method == 'POST':
        form = HallForm(request.POST)
        if form.is_valid():
            hall = form.save(commit=False)
            hall.is_available = 'status' in request.POST and request.POST['status'] == 'available'
            hall.save()
            messages.success(request, 'Hall created successfully!')
            return redirect('hall_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = HallForm(initial={'is_available': True})
    
    context = {
        'form': form,
    }
    return render(request, 'hall/new_hall_creation.html', context)

@login_required
def facility_creation(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Facility created successfully!')
            return redirect('hall:facility_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FacilityForm()
    
    context = {
        'form': form,
    }
    return render(request, 'hall/facility_creation.html', context)

@login_required
def facility_list(request):
    facilities = Facility.objects.all()
    context = {
        'facilities': facilities
    }
    return render(request, 'hall/facility_list.html', context)

@login_required
def event_type_creation(request):
    if request.method == 'POST':
        form = EventTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event type created successfully!')
            return redirect('hall:event_type_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EventTypeForm()
    
    context = {
        'form': form,
    }
    return render(request, 'hall/event_type_creation.html', context)

@login_required
def event_type_list(request):
    event_types = EventType.objects.all()
    context = {
        'event_types': event_types
    }
    return render(request, 'hall/event_type_list.html', context)

@login_required
def hall_list(request):
    halls = Hall.objects.all()
    context = {
        'halls': halls
    }
    return render(request, 'hall/hall_list.html', context)
