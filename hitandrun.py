import numpy as np
from scipy.spatial.distance import norm


class HitandRun:
    def __init__(self, polytope, startPoint):
        # init core varaibles
        self.polytope = polytope
        self.startingPoint = startPoint

        # set run point
        self.runningPoint = startPoint
        self.direction = self.getDirection()
        self.sampleResult = []

    def getDirection(self):
        #set a random direction to point to
        direction = np.random.randn(self.polytope.dimension)
        # 2-norm used (vector)
        return direction / norm(direction)

    def samplePoints(self, n):
        self.n = n
        result = []
        for i in range(self.n):
            self.runningPoint = self.takeStep()
            result.append(list(self.runningPoint))
        return result

    def takeStep(self):
        self.direction = self.getDirection() #direction
        print("Direction =: " + str(self.direction))
        lambdas = self.getLambdas() #distance

        positiveLambdas = np.min(lambdas[lambdas > 0])
        negativeLambdas = np.max(lambdas[lambdas < 0])

        #random in 2 lambdas and calculate new point
        ranDistance = np.random.uniform(low=negativeLambdas, high=positiveLambdas)
        return self.runningPoint + ranDistance * self.direction


    def getLambdas(self):
        #get travel distance for the certain direction from (current) starting point
        a = self.polytope.a
        p = self.polytope.auxPoints

        lambdas = []
        for i in range(self.polytope.planes):
            if np.isclose(self.direction @ a[i], 0):
                lambdas.append(np.nan)
            else:
                lambdas.append((p[i] - self.runningPoint) @ a[i] / self.direction @ a[i])

        return np.array(lambdas)

