from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def mosaic(request):
    return HttpResponse("Mosaic API")

def mosaic_page(request):
    template = loader.get_template('tools/mosaic.html')
    context = {}
    return HttpResponse(template.render(context, request))