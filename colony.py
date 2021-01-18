
class Colony(object):
    def __init__(self, alpha: float, beta: float, rho: float, Q: int, scheme: int):
        """
        :param alpha: Pheromone parameter to regulate the influence of the intensity of pheromone trails between sites.
        :param beta: Local node parameter to regulate the influence of the visibility between sites.
        :param rho: Pheromone evaporation factor to regulate the reduction of pheromone.
        :param Q: Pheromone deposit factor
        :param scheme: pheromone update procedure.
            0: ant-ranking system
            1: ant-colony system
            2: ant-elitist system
        """
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.scheme = scheme
