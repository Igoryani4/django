from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'hw2/upload_image.html', {'form': form})
