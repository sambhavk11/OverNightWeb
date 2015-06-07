from django.shortcuts import render
import json
from django.http import HttpResponse
import api_call

# Create your views here.
def landing_page(request):
    return render(request, 'landingPage.html')

# api call to alchemy to get content
def get_content(request):
    print "here"
    res = ''
    if request.method == 'POST':
        params = request.POST
        val = params.get('val')
        print val
        res = api_call.getNews(val)
        print "outside"
    # return HttpResponse(json.dumps({'data': res}), content_type="application/json")
    return render(request, 'landingPage.html', {'data': res})
