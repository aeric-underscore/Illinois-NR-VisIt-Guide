from visit import *
  
OpenDatabase("/path/to/sample_vector_field.vtk")
AddPlot("Vector", "vec_field")

v = VectorAttributes()
v.scaleByMagnitude = 0
v.autoScale = 0
v.scale = 2.0
v.minFlag = 1
v.maxFlag = 1
v.min = 0
v.max = 1e-8
v.colorTableName = 'hot'
v.nVectors = 1000
SetPlotOptions(v)

c = View3DAttributes()
c.viewNormal = (1.0, -1.0, 0.35)
c.viewUp = (0, 0, 1)
SetView3D(c)
s = SaveWindowAttributes()
s.format = s.PNG
s.outputToCurrentDirectory = 1
s.fileName = "/path/to/output"
SetSaveWindowAttributes(s)
DrawPlots()
SaveWindow()
