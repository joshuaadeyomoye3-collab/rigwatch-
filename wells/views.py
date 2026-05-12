from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Well

def well_list(request):
    wells = Well.objects.filter(active=True).order_by('name')
    context = {
        'wells':          wells,
        'critical_count': Well.objects.filter(status='CRITICAL').count(),
        'total_count':    Well.objects.count(),
    }
    return render(request, 'wells/well_list.html', context)

def well_detail(request, well_id):
    well = get_object_or_404(Well, id=well_id)
    return render(request, 'wells/well_detail.html', {'well': well})

def well_status(request, well_id):
    well = get_object_or_404(Well, id=well_id)
    return HttpResponse(f'{well.name} status: {well.status}')