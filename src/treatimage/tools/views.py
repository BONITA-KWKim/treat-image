from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File

from PIL import Image

from .forms import UploadImageForm
from .models import UploadImage, ProcessedImage
import os
# Create your views here.
@csrf_exempt
@require_http_methods(["GET", "POST"])
def mosaic(request):
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            # process image treat
            ## save raw image (uploadimage table)
            instance = UploadImage(raw_image=request.FILES['raw_image'])
            instance.save()

            ## image processing
            after_name = 'mosaic_' + request.FILES['raw_image'].name

            im = Image.open(request.FILES['raw_image'])
            size = (64, 64)
            im.thumbnail(size)
            ## save temporary image file
            im.save('tmp/' + after_name)

            ## save processed image (processedimage table)
            f = open('tmp/' + after_name, 'rb')
            myImage = File(f)

            instance = ProcessedImage()
            instance.processed.save(after_name, myImage)
            instance.save()

            f.close()
            ## remove tmp image
            os.remove('tmp/' + after_name)

            return HttpResponse("success to save a image")
        return HttpResponse("invalid request")
    return HttpResponse("Mosaic API")

def mosaic_page(request):
    template = loader.get_template('tools/mosaic.html')
    context = {}
    return HttpResponse(template.render(context, request))