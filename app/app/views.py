from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
import os

from django.conf import settings

from .services import *




def main(request):

	message = ''
	context = {}
	


	if request.method == 'POST':
		
		form = UploadFileForm(request.POST, request.FILES)

		if form.is_valid():
			name = request.FILES['file'].name
			if name.endswith('.zip'):
				path = settings.MEDIA_ROOT
				fullPath =  settings.MEDIA_ROOT + request.FILES['file'].name

				pic = handle_uploaded_file(request.FILES['file'], fullPath, path)
				if not name == 'fields_test.zip':
					message = 'File {0} was succesfully imported to database and rendered..'.format(name)
				else:
					message = 'File {0} was succesfully imported to database and rendered by [productivi] attribute..'.format(name)					
				return render(request, 'main.html', {'form': form, 'message':message, 'pic': pic, 'folder': settings.MEDIA_ROOT})
			else:
				message = 'File must be an archive ".zip" '
				return render(request, 'main.html', {'form': form, 'message':message})
	else:

		form = UploadFileForm()

	return render(request, 'main.html', {'form': form, 'message':message})

