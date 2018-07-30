from zipfile import ZipFile
 
 
def upzip_file(file_name, path):

	with ZipFile(file_name, 'r') as zip:
		# printing all the contents of the zip file
		#zip.printdir()
	 
		#print('Extracting all the files now...')
		zip.extractall(path)
		#print('Done!')



def handle_uploaded_file(f, full_path, path):

	with open(full_path, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

	
	upzip_file(full_path, path)
	

	return f.name
		
