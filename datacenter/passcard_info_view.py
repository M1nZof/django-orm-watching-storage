from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from datacenter.time_functions import get_duration, format_time


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    for visit in passcard_visits:
      total_seconds = get_duration(visit)
      hours = int(round(total_seconds // 3600))
      if hours >= 1:
        is_strange = True
      else:
        is_strange = False
      duration = format_time(total_seconds)
      visit_parameters = {
        'entered_at': visit.entered_at,
        'duration': duration,
        'is_strange': is_strange
      }
      this_passcard_visits.append(visit_parameters)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
