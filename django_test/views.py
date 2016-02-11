from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Template,Context
from django.shortcuts import render_to_response 

def request_parameters(request):
    values = request.META.items()
    values.sort()
    html = []
    print "*************GET",request.GET
    print "**************POST",request.POST
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

# In this we are demonstrating the inheritance of templates. The base template has been inherited by the inherit_base.html
def trial_inheritance_render(request):
    return render_to_response('inherit_base.html',{
                                                   })

# In this case we will load and render the template and send the html response in one line
def current_datetime_render_response(request):
    print "-------------------------This is being loaded,rendered and responded in a single statement -------------------------------------"
    # we can also use python function locals. This is used
    return render_to_response ('current_datetime.html',{'name':"Shivam Goyal",
                                                        'current_date':datetime.datetime.now(),
                                                        'include_name':'Django',
                                                        }) 

# This is to demonstrate how to pass local variables into dictionary as a parameter 
def current_dateime_render_response_local(request):
    name = 'Shivam Goyal'
    include_name = "Django"
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html',locals())


# In this case we are first loading the template then rendering it and then sending an html response
def current_datetime_file(request):
    t = get_template('current_datetime.html')
    c = Context({'name':'Shivam Goyal',
                 'current_date':datetime.datetime.now(),
                 'include_name':'Django'
                 })
    html = t.render(c)
    return HttpResponse(html)
    
def hello(request):
    return HttpResponse("Hello world")

def current_datetime_template(request):
    t = Template('''
        This is a design rendered by template engine. Hello My name is {{name}}. Today the date is {{current_date|date:'F Y,j'}}
    ''')
    c = Context({'name':"Shivam Goyal",'current_date':datetime.datetime.now()})
    return HttpResponse(t.render(c))

def current_datetime(request):
    html= '''<html><body>
                The current datetime is %s
            </body></html>'''%(datetime.datetime.now())
    return HttpResponse(html)


def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)    