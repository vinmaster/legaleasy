from django.shortcuts import render, render_to_response, HttpResponse, redirect, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from translator.models import Good, Bad

# Views here
@csrf_protect
def home(request):
    return render_to_response("translator/home.html", {}, context_instance=RequestInstance(request))

@csrf_protect
def translate(request):
    finished_string = ''
    from_text = request.POST['block'].split()
    for i in from_text:
        try:
            found_bad_word = Bad.objects.get(pk=from_text)
            found_good_word = Good.objects.get(found_bad_word.maps)
            found_bad_word[i] = found_good_word.text
        except Bad.DoesNotExist:
            continue
        except Good.DoesNotExist:
            continue
    for j in from_text:
        finished_string = finished_string + ' ' + i
    return HttpResponse(finished_string)


