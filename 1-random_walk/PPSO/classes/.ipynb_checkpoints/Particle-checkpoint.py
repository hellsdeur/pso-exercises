import numpy as np
import copy

class Particle:
    
    # contructor
    def __init__(self, f, DIM, RANGE, n = None, x = None):
        if n is not None:
            self.n = n
        else:
            self.n = DIM
            
        # store objective function
        self.f = f
        
        self.DIM = DIM
        self.RANGE = RANGE
        
        # start position at random
        if x is not None:
            self.x = x * np.ones(self.n) # change to array-like
        else:               
            self.x = self.RANGE[0] + (self.RANGE[1] - self.RANGE[0]) * np.random.random(self.n)
            
        # evaluate position
        self.evaluate()

        # start velocity with 0
        self.v = np.zeros(self.n)

        # deep copy the current position as best personal and fitness
        self.m = copy.deepcopy(self.x)
        self.fit_m = self.fit_x
        
    def __str__(self):
        return "X: " + str([round(i, 4) for i in self.x]) + \
               "\nFITX: " + str("{:.4e}".format(self.fit_x))
#               "\nM: " + str([round(i, 4) for i in self.m]) + \
#               "\nFITM: " + str("{:.4e}".format(self.fit_m)) + \
#               "\nV: " + str([round(i, 4) for i in self.v])
               
    def getCopy(self):
        return copy.deepcopy(self)
    
    def evaluate(self):
        self.fit_x = self.f(self.x)