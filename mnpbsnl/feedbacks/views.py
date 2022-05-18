from django.shortcuts import render, HttpResponse

from .models import Mobile    #, Circle, Ssa

# Create your views here.
def home(request):
    return HttpResponse("Hello world from Django, Gunicorn, Docker and NGINX")

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    mob_count = Mobile.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'mob_count': mob_count,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

