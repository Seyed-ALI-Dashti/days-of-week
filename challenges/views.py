from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

days = {
    'saturday': 'This is saturday',
    'sunday': 'This is sunday',
    'monday': 'This is monday',
    'tuesday': 'This is tuesday',
    'wednesday': 'This is wednesday',
    'thursday': 'This is thursday',
    'friday': 'This is friday',
}


def dynamic_days(request, day):
    day_data = days.get(day)

    if day_data is None:
        raise Http404
        # response_data = render_to_string('404.html')
        # return HttpResponseNotFound(response_data)

    context = {
        'day_data': day_data,
        "day_name": day.upper,
    }
    return render(request, 'challenges/challenge.html', context)



def days_list(request):
    days_list = list(days.keys())
    context = {
        'days': days_list
    }
    return render(request, "challenges/index.html", context)


def dynamic_days_by_number(request, day):
    if day > len(days) or day == 0:
        return HttpResponseNotFound('day is not exist')
    days_name = list(days.keys())
    redirect_days = days_name[day - 1]
    redirect_url = reverse('days-of-week', args=[redirect_days])
    return HttpResponseRedirect(redirect_url)
