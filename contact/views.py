from django.shortcuts import render
from models import ContactForm
from django.template import RequestContext
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import Template,Context

def named_arguments_trial(request,year,month,template_name):
    print "********************template_name",template_name 
    html = Template('''
    <p>Year: {{year}}</p>
    <p>Month: {{month}}</p>
    ''')
    c= Context({'year':year,'month':month})
    return HttpResponse(html.render(c))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['shivam_1111@hotmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render(request, 'contact_form.html', {'form': form},context_instance=RequestContext(request))

