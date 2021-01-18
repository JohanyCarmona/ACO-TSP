import random
import math

"""
Graph contains information about cost matrix and pheromoneSpace status.
"""
class Graph(object):
    def __init__(self, locations: list, GLPK: bool = False):
        """
        :param costMatrix: distances between all sites on the graph.
        :param pheromoneSpace: pheromone value for each trail on the graph.
        :param GLPK: indicates if the graph will be used to generate a GLPK format data file, that can be used to solve using GLPK model (tsp.mod)
        """
        self.GLPK = GLPK
        self.totalSites = len(locations)
        
        #Initialize matrix with distances between sites.
        self.costMatrix = [ [ self.cost(locations[i] , locations[j]) if i != j else 0 for j in range(self.totalSites) ] for i in range(self.totalSites) ]
        
        #Initialize matrix with a residual pheromone value for each status on the graph.
        self.pheromoneSpace = [[1/self.totalSites**2 if self.totalSites != 0 else -1]*self.totalSites]*self.totalSites
        
    #Generate Euclidean cost from bidimentional space.
    def cost(self, originLocation: tuple, destinyLocation: tuple):
        cost = math.sqrt((originLocation[0] - destinyLocation[0]) ** 2 + (originLocation[1] - destinyLocation[1]) ** 2)
        return cost if not(self.GLPK) else round(cost)
            
