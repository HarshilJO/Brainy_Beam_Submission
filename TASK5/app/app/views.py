from django.shortcuts import render
from django.http import JsonResponse
from .models import BlackAndWhiteImage
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
@csrf_exempt
def convert_to_bw(request):
    if request.method == 'POST' and request.FILES['image']:
        original_image = request.FILES['image']
        img = Image.open(original_image)
        bw_img = img.convert('L')
        buffer = io.BytesIO()
        bw_img.save(buffer, format='PNG')
        bw_file = InMemoryUploadedFile(buffer, None, 'bw_image.png', 'image/png', buffer.getbuffer().nbytes, None)
        bw_image = BlackAndWhiteImage(original_image=original_image, bw_image=bw_file)
        bw_image.save()
        return JsonResponse({'message': 'Image converted and saved successfully', 'id': bw_image.id})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)