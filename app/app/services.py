from zipfile import ZipFile
import os
import ogr
import gdal
from .config import *
from .render import *

"""Importing shapefile to a database"""

#---------------------------------
conn = [SERVERNAME,DB,PORT,USER,PASSWORD,TABLE]

gdal.SetConfigOption('CPL_DEBUG','ON')

def testLoad(serverDS, table, sourceFile):
	ogr.RegisterAll()
	shapeDS = ogr.Open(sourceFile)
	sourceLayer = shapeDS.GetLayerByIndex(0)
	options = []
	name = serverDS.CopyLayer(sourceLayer,table,options).GetName()


def import_to_db(shapefile, tableName):
	tableName = TABLE
	connectionString = "PG:dbname='%s' host='%s' port='%s' user='%s' password='%s'" % (conn[1],conn[0],conn[2],conn[3],conn[4])
	ogrds = ogr.Open(connectionString)
	name = testLoad(ogrds, tableName, shapefile)
#----------------------------------	

"""Getting shapefile name to work with"""
#--------------------------------

def getShapefilename(path):

	dirs = os.listdir(path)

	for file in dirs:
		if file.endswith('.shp'):
			shapefile = str(file)

	return shapefile
#---------------------------------

"""Unzipping the archive"""
#----------------------------------

def upzip_file(file_name, path):

	with ZipFile(file_name, 'r') as zip:
		zip.extractall(path)

	shapefileName = getShapefilename(path)	

	shapefile = path + shapefileName

	return shapefile

#-----------------------------------

"""Main handler function"""
#-----------------------------------
def handle_uploaded_file(f, full_path, folder):

	with open(full_path, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

	
	shapefile = upzip_file(full_path, folder)
	tableName = TABLE
	import_to_db(shapefile, tableName)
	pic = render_image(conn, folder, PIC_NAME)

	return pic


#-----------------------------------
	
		
