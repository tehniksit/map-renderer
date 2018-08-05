import mapnik

def render_image(conn, folder, pic):

	m = mapnik.Map(450,450)
	m.background = mapnik.Color("White")
	r = mapnik.Rule()
	s = mapnik.Style()

	polygon_symbolizer = mapnik.PolygonSymbolizer()
	polygon_symbolizer.fill = mapnik.Color('Grey')
	r.symbols.append(polygon_symbolizer)

	productivi_less_30 = mapnik.Rule()
	productivi_less_30.filter = mapnik.Expression("[productivi]<=30")
	productivi_less_30_polygon_symbolizer = mapnik.PolygonSymbolizer()
	productivi_less_30_polygon_symbolizer.fill = mapnik.Color('#ff5959')
	productivi_less_30.symbols.append(productivi_less_30_polygon_symbolizer)

	productivi_30_70 = mapnik.Rule()
	productivi_30_70.filter = mapnik.Expression("([productivi]>=31) and ([productivi]<70)")
	productivi_30_70_polygon_symbolizer = mapnik.PolygonSymbolizer()
	productivi_30_70_polygon_symbolizer.fill = mapnik.Color('#ffa159')
	productivi_30_70.symbols.append(productivi_30_70_polygon_symbolizer)

	productivi_more_then_70 = mapnik.Rule()
	productivi_more_then_70.filter = mapnik.Expression("[productivi]>=70")
	productivi_more_then_70_polygon_symbolizer = mapnik.PolygonSymbolizer()
	productivi_more_then_70_polygon_symbolizer.fill = mapnik.Color('#d0ff59')
	productivi_more_then_70.symbols.append(productivi_more_then_70_polygon_symbolizer)
	
	s.rules.append(productivi_less_30)
	s.rules.append(productivi_30_70)
	s.rules.append(productivi_more_then_70)

	m.append_style('My Style',s)

	layer = mapnik.Layer("Data from PostGIS")


	layer.datasource = mapnik.PostGIS(dbname=conn[1], host=conn[0], port=conn[2], table = conn[5], user=conn[3], password=conn[4])
	layer.styles.append('My Style')
	m.layers.append(layer)
	m.zoom_all()
	mapnik.render_to_file(m, folder + pic, 'png')

	return pic
