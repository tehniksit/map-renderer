from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
import os

from django.conf import settings

def handle_uploaded_file(f, path):

	with open(path, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)




def main(request):

	message = ''
	context = {}

	if request.method == 'POST':
		
		form = UploadFileForm(request.POST, request.FILES)

		if form.is_valid():
			name = request.FILES['file'].name
			if name.endswith('.zip'):
				fullPath =  settings.MEDIA_ROOT + request.FILES['file'].name
				handle_uploaded_file(request.FILES['file'], fullPath)
				message = 'File succesfully uploaded'
				return render(request, 'main.html', {'form': form, 'message':message})
			else:
				message = 'File must be an archive ".zip" '
				return render(request, 'main.html', {'form': form, 'message':message})
	else:

		form = UploadFileForm()

	return render(request, 'main.html', {'form': form, 'message':message})

