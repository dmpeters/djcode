from django.template.loader import get_template
from django.template import Context
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import datetime



def hello(request):
    # say hello
    return HttpResponse("Hello, welcome to my %s page" % request.path)

# current_datetime w/o template
def current_datetime(request):
    # get the current time
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    
    return HttpResponse(html)

# current_datetime w/ template
def current_datetime_template(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def more_current_datetime_template(request):
    now = datetime.datetime.now()
    return render_to_response('more_current_datetime.html', {'current_date': now})

def hours_ahead(request, hours):
    # time ahead by said hours
    try:
        hours = int(hours)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=hours)
    return render_to_response('hours_ahead.html', {'hours_offset': hours, 'next_time': dt})

