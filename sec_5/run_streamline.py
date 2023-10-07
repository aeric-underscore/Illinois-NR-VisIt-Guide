import numpy as np
from visit import *

R = 10.; num_pts = 8
thetas = np.linspace(0, 2*np.pi, num_pts)
xs = R*np.cos(thetas)
ys = R*np.sin(thetas)
zs = 0*thetas
points = []
for i in range(num_pts):
    points.append(xs[i])
    points.append(ys[i])
    points.append(zs[i])
    
OpenDatabase("/path/to/sample_vector_field.vtk")
AddPlot("Pseudocolor", "vec_field")
AddOperator("IntegralCurve")

l = IntegralCurveAttributes()
l.sourceType = l.PointList
l.pointList = tuple(points)

SetOperatorOptions(l)
c = View3DAttributes()
c.viewNormal = (1.0, -0.35, 0.35)
c.viewUp = (0, 0, 1)
SetView3D(c)
s = SaveWindowAttributes()
s.format = s.PNG
s.outputToCurrentDirectory = 1
s.fileName = "/path/to/output"
SetSaveWindowAttributes(s)
DrawPlots()
SaveWindow()
