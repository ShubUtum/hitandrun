
import numpy as np
import polytope
import hitandrun

a = np.array([[1,0], [-1,0], [0,1], [0,-1]], dtype=np.float64)
b = np.array([1,1,1,1], dtype=np.float64)
start = np.array([-.5, -.5], dtype=np.float64)
p = polytope.Polytope(a,b)

runner = hitandrun.HitandRun(p, start)
result = runner.samplePoints(100)
