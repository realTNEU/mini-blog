from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UploadedFile

@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        
        file_obj = UploadedFile(
            file=uploaded_file,
            uploader=request.user
        )
        file_obj.save()
        
        messages.success(request, f'File "{uploaded_file.name}" uploaded successfully!')
        return redirect('files:list_files')
    
    return render(request, 'files/upload_file.html')

def list_files(request):
    files = UploadedFile.objects.all()
    return render(request, 'files/list_files.html', {'files': files})
