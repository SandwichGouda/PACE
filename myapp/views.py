from django.shortcuts import render
from django.http import FileResponse, Http404, HttpResponseRedirect
import os
from django.conf import settings
from django.contrib.staticfiles import finders

# Create your views here.

def index(request):
    return render(request, 'index.html')

def admin(request):
    return render(request, 'admin.html')

def pace2023(request):
    return render(request, 'PACE2023.html')

def serve_pdf(request, filename):
    
    # Construct the full file path
    file_path = os.path.join(settings.MEDIA_ROOT, 'pdfs',filename)

    # Check if the file exists
    if not os.path.exists(file_path):
        raise Http404(file_path,filename)
        #raise Http404("File not found")

    # Return a response to display the PDF in the browser
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')

def list_pdfs(request):
    # Chemin vers le dossier 'pdfs' dans le répertoire 'static'
    pdf_directory = os.path.join(settings.BASE_DIR, 'media', 'pdfs')
    
    # Liste des fichiers PDF dans le dossier
    pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]
    from random import shuffle
    shuffle(pdf_files)
    
    context = {
        'pdf_files': pdf_files
    }
    return render(request, 'pace2023.html', context)

# def serve_pdf(request, filename):
#     # Define the path where the PDF files are stored
#     # file_path = os.path.join('myapp', 'static', 'myapp', 'pdfs', f"{filename}.pdf")

#     #if request.path.endswith('/'):
#     #    return HttpResponseRedirect(request.path.rstrip('/'))

#     file_path = finders.find(f"myapp/static/myapp/pdfs/{filename}") # !! filename or filename.pdf ?

#     # Check if the file exists and serve it; raise 404 if it doesn’t
#     if os.path.exists(file_path):
#         return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
#     else:
#         raise Http404("PDF file not found.")
