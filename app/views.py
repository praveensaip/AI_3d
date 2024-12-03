from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import UploadedImage, FashionShowSettings,UploadedMusic
from .ai import map_clothing_to_model

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image') and request.FILES.get('music'):
        image = request.FILES['image']
        music = request.FILES['music']
        
        try:
            # Save image and music to the model (assuming models for both)
            uploaded_image = UploadedImage.objects.create(image=image)
            uploaded_music = UploadedMusic.objects.create(music=music)

            # Assuming you have a method to map clothing to a 3D model
            result = map_clothing_to_model(uploaded_image.image.path, "model_path_placeholder")
            print("image path", uploaded_image.image.path)

            #demo
            # Return the image and music URLs in the response
            return redirect('fashion_show') 

        except Exception as e:
            return JsonResponse({'message':str(e)})
        
    return render(request, 'upload_image.html')


def customize_show(request):
    if request.method == 'POST':
        theme = request.POST.get('theme')
        music = request.POST.get('music')
        if not theme or not music:
            return JsonResponse({"status": "error", "message": "Theme and music are required"}, status=400)
        
        try:
            FashionShowSettings.objects.create(theme=theme, music=music)
            return JsonResponse({"status": "success", "message": "Show customized!"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    
    return render(request, 'customize_show.html')

def fashion_show(request):
    # Get the latest uploaded image and music (or handle as per your logic)
    uploaded_image = UploadedImage.objects.last()  # Or use filter to get specific image
    uploaded_music = UploadedMusic.objects.last()  # Or use filter to get specific music
    
    # Get the URLs for the image and music
    image_url = uploaded_image.image.url if uploaded_image else None
    music_url = uploaded_music.music.url if uploaded_music else None
    
    # Pass the URLs to the template
    return render(request, 'fashion_show.html', {
        'image_url': image_url,
        'music_url': music_url
    })
