from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@require_http_methods(["GET", "POST"])
def mosaic(request):
    if request.method == "POST":
        result_str = "POST Method in mosaic API: " + str(request.read())
        return HttpResponse(result_str)

    return HttpResponse("Mosaic API")

def mosaic_page(request):
    template = loader.get_template('tools/mosaic.html')
    context = {}
    return HttpResponse(template.render(context, request))