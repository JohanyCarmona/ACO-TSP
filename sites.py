import random
from graph import Graph

class Sites(object):
    def __init__(self, filename: str, GLPK: bool = False, totalSites: int = None, longitudeRange: tuple = None, latitudeRange: tuple = None):
        self.GLPK = GLPK
        self.sites = []
        if GLPK is False and totalSites is None and longitudeRange is None and latitudeRange is None:
            self.importSites(filename)
        else:
            self.sites = self.generateSites(totalSites, longitudeRange, latitudeRange)
            self.exportSites(filename)
            if GLPK: self.exportSitesGLPK(filename)
            
    def generateSites(self, totalSites: int, longitudeRange: tuple, latitudeRange: tuple):
        return [dict( index = i, name = "site{}".format(i), location = ( self.randomRange(longitudeRange), self.randomRange(latitudeRange) ) ) for i in range(totalSites)]
        
    def generateRoute(self, path: list):
        return [self.sites[indexPath]['index'] for indexPath in path]
    
    def generatePath(self, route: list):
        routePath = [indexPath['index'] for indexPath in self.sites]
        return [routePath.index(index) for index in route]
    
    def getLocations(self):
        return [self.sites[i]['location'] for i in range(len(self.sites))]
        
    def importSites(self, filename : str):
        with open("./data/{}.dat".format(filename)) as file:
            fileContent = file.readlines()
            for line in fileContent:
                site = line.split(',')
                self.sites.append(dict(index = int(site[0]), name = str(site[1]), location = (float(site[2]), float(site[3]))))
                
    def exportSites(self, filename : str):
        with open("./data/{}.dat".format(filename), "w") as file:
            i = 0 if not(self.GLPK) else 1
            for site in self.sites:
                line = [str(site['index'] + i), str(site['name']), str(site['location'][0]),str(site['location'][1])]
                file.writelines(','.join(line))
                file.writelines('\n')
    
    def exportSitesGLPK(self, filename : str):
        with open("./data/GLPK/{}.dat".format(filename), "w") as file:
            file.writelines('data;\n')
            totalSites = len(self.sites)
            file.writelines('param n := {};\n'.format(totalSites))
            file.writelines('param : E : c :=\n')
            graph = Graph(self.getLocations(), GLPK = True)
            for i in range(totalSites):
                for j in range(totalSites):
                    if i != j:
                        file.writelines('\t{}\t{}\t{}\n'.format(i+1,j+1,graph.costMatrix[i][j]))
            file.writelines(';\n')
            file.writelines('end;\n')  
        
    def randomRange(self, range: tuple):
        return float(range[0]) + float((range[1] - range[0])) * random.random()
