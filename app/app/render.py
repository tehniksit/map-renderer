import mapnik

def render_image(conn, folder, pic):

	m = mapnik.Map(300,300)
	m.background = mapnik.Color("Grey")
	r = mapnik.Rule()
	s = mapnik.Style()
	polygon_symbolizer = mapnik.PolygonSymbolizer()
	polygon_symbolizer.fill = mapnik.Color('#f2eff9')
	r.symbols.append(polygon_symbolizer)

	line_symbolizer = mapnik.LineSymbolizer()
	line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')
	line_symbolizer.stroke_width = 0.1

	r.symbols.append(line_symbolizer)
	s.rules.append(r)
	m.append_style('My Style',s)

	layer = mapnik.Layer("Data from PostGIS")


	layer.datasource = mapnik.PostGIS(dbname=conn[1], host=conn[0], port=conn[2], table = conn[5], user=conn[3], password=conn[4])
	layer.styles.append('My Style')
	m.layers.append(layer)
	m.zoom_all()
	mapnik.render_to_file(m, folder + pic, 'png')

	return pic
