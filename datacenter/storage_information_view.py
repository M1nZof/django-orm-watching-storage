from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from datacenter.time_functions import get_duration, format_time


def storage_information_view(request):
    non_closed_visits = []
    employees_in_storage = Visit.objects.filter(leaved_at=None)
    for employee in employees_in_storage:
        employee_in_storage_name = employee.passcard
        total_seconds = get_duration(employee)
        duration = format_time(total_seconds)
        non_closed_visits_parameters = {
                'who_entered': employee_in_storage_name,
                'entered_at': employee.entered_at,
                'duration': duration
        }
        non_closed_visits.append(non_closed_visits_parameters)
      
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
