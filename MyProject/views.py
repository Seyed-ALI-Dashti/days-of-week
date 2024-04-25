from django.http import HttpResponse


def index(request):
    # response_data = f'<a href="days-of-week/1" target="_blank"> Saturday </a>'
    return HttpResponse("Index Page MyProject")