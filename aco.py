import random
from graph import Graph
from colony import Colony
from ant import Ant
"""
Ant Colony Optimization (ACO) contains the Metaheuristic model in charge of apply diversification and intensifications techniques to obtain the best solution on the Travelling Salesman Problem (TSP).
"""
class ACO(object):
    def __init__(self, iterations: int, totalAnts: int, alpha: float, beta: float, rho: float, Q: int, scheme: int):
        """
        :param iterations
        :param totalAnts
        :param colony 
        """
        self.iterations = iterations
        self.totalAnts = totalAnts
        self.colony = Colony(alpha, beta, rho, Q, scheme)
        
    #Updating the Pheromone Space where is all the pheromone deposited for each ants of the colony.
    def updatePheromoneSpace(self, graph: Graph, ants: list):
        for ant in ants:
            for i in range(graph.totalSites):
                for j in range(graph.totalSites):
                    graph.pheromoneSpace[i][j] = self.colony.rho * graph.pheromoneSpace[i][j] + ant.deltaPheromone[i][j]
    
    def solveModel(self, graph: Graph):
        """
        :param graph
        """
        bestCost = float('inf')
        bestSolution = []
        for iteration in range(self.iterations):
            ants = [Ant(self.colony, graph) for i in range(self.totalAnts)]
            for ant in ants:
                for i in range(graph.totalSites - 1):
                    #Next movement according visibility allowed nodes.
                    ant.nextMovement()
                #End movement from end node to start node.
                ant.totalCost += graph.costMatrix[ant.tabu[-1]][ant.tabu[0]]
                if ant.totalCost < bestCost:
                    bestSolution = ant.tabu
                    bestCost = ant.totalCost
                ant.updateDeltaPheromone()
            self.updatePheromoneSpace(graph, ants)
        return bestSolution, bestCost

