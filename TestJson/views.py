from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from .forms import ContactForm
from .models import Email


# 1. Submit initial data in a form
def submit_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.save()
        return JsonResponse({'result': 'The form has been submitted!'})

    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})


# 2. Serialize data submitted from the DB (JSON response)
def serialize(request):
    model_as_json = serializers.serialize('json', Email.objects.all())
    return HttpResponse(model_as_json, content_type='application/json')


# 3. Validate whether e_mail has already been submitted
def validate(request):
    e_mail = request.GET.get('e_mail', None)
    data = {
        'was_submitted': Email.objects.filter(e_mail__iexact=e_mail).exists()
    }
    return JsonResponse(data)




