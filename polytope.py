import numpy as np


class Polytope:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.dimension = a.shape[1]  # polytope dimension (col)
        self.planes = a.shape[0]  # polytope nplane (row)

        self.getPlanesAuxPoints()

    def getPlanesAuxPoints(self):
        auxPoints = []
        for i in range(self.planes):
            auxPoints.append(self.getAuxiliarPoints(self.a[i], self.b[i]))
        self.auxPoints = auxPoints

    def getAuxiliarPoints(self, a, b):
        p = np.zeros(self.dimension)
        i = np.argmax(a != 0)  # remove neg
        p[i] = b / a[i]
        return p