from zipfile import ZipFile
import os
import ogr
import gdal
from .config import *

gdal.SetConfigOption('CPL_DEBUG','ON')

def testLoad(serverDS, table, sourceFile):
	ogr.RegisterAll()
	shapeDS = ogr.Open(sourceFile)
	sourceLayer = shapeDS.GetLayerByIndex(0)
	options = []
	name = serverDS.CopyLayer(sourceLayer,table,options).GetName()


def import_to_db(shapefile, tableName):
	serverName = SERVERNAME
	database = DB
	port = PORT
	usr = USER
	pw = PASSWORD
	table = tableName
	connectionString = "PG:dbname='%s' host='%s' port='%s' user='%s' password='%s'" % (database,serverName,port,usr,pw)
	ogrds = ogr.Open(connectionString)
	name = testLoad(ogrds,table, shapefile)
	

def getShapefilename(path):

	dirs = os.listdir(path)

	for file in dirs:
		if file.endswith('.shp'):
			shapefile = str(file)

	
	return shapefile


def upzip_file(file_name, path):

	with ZipFile(file_name, 'r') as zip:
		zip.extractall(path)

	shapefileName = getShapefilename(path)	

	shapefile = path + shapefileName

	return shapefile


def handle_uploaded_file(f, full_path, folder):

	with open(full_path, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

	
	shapefile = upzip_file(full_path, folder)
	tableName = 'shape-table1'
	import_to_db(shapefile, tableName)

	
		
