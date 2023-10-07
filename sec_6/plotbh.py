from visit import *

x0, y0, z0 = 0., 0., 0. #center of mass of black hole
OpenDatabase("/path/to/bh1.3d")
OpenDatabase("/path/to/spinvec.vtk")
ActivateDatabase("/path/to/bh1.3d")
AddPlot("Pseudocolor", "bh1")  #plot index 0
ActivateDatabase("/path/to/spinvec.vtk")
AddPlot("Vector", "spinvec")   #plot index 1

SetActivePlots(0)  #only apply options/operators to bh1 plot
Pseudo = PseudocolorAttributes()
Pseudo.colorTableName = "gray"
SetPlotOptions(Pseudo)
AddOperator("Delaunay")

SetActivePlots(1) #only apply options/operators to spinvec plot
Vec = VectorAttributes()
Vec.glyphLocation = Vec.UniformInSpace
Vec.autoScale = 0
Vec.scale = 110
Vec.colorByMag = 0  #use constant color
Vec.vectorColor = (0, 255, 0, 255) #green
SetPlotOptions(Vec)
AddOperator("Box")
BoxAtts = BoxAttributes()
BoxAtts.minx = x0 - 0.0005
BoxAtts.maxx = x0 + 0.0005
BoxAtts.miny = y0 - 0.0005
BoxAtts.maxy = y0 + 0.0005
BoxAtts.minz = z0 - 0.0005
BoxAtts.maxz = z0 + 0.0005
SetOperatorOptions(BoxAtts)

a = AnnotationAttributes()
a.backgroundMode = a . Solid
a.backgroundColor = (155, 155, 155, 255) # gray
SetAnnotationAttributes(a)
c = View3DAttributes()
c.viewNormal = (0.5, -1, 0)
c.imageZoom = 300
c.viewUp = (0, 0, 1)
SetView3D(c)
s = SaveWindowAttributes()
s.format = s.PNG
s.outputToCurrentDirectory = 1
s.fileName = "/path/to/output"
SetSaveWindowAttributes(s)
DrawPlots()
SaveWindow()
