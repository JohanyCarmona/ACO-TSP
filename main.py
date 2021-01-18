from aco import ACO
from graph import Graph
from plot import plot
from sites import Sites
import random
import sys
import time

def main(args):
    if len(args) == 1:
        helpMessage()
    
    #generateSites: It generates a file with a randomly set of Sites according the range specified by user.
    elif args[1] == 'generateSites':
        try:
            GLPK = True if args[2] == 'GLPK' else False
            enable = 1 if GLPK == True else 0
            filename = str(args[2 + enable])
            totalSites = int(args[3 + enable])
            longitudeRange = (float(args[4 + enable]),float(args[5 + enable]))
            latitudeRange = (float(args[6 + enable]),float(args[7 + enable]))
            sites = Sites(filename, GLPK, totalSites,longitudeRange,latitudeRange)
            print("Info: {}.dat file created succesfully".format(filename))
        except:
            helpMessage()
    
    #solveModel: It solves the TSP problem using Ant Colony Optimization according the ACO parameters gived by user.
    elif args[1] == 'solveModel':
        try:
            GLPK = True if args[2] == 'GLPK' else False
            enable = 1 if GLPK == True else 0
            filename = str(args[2 + enable])
            iterations = int(args[3 + enable])
            totalAnts = int(args[4 + enable])
            alpha = float(args[5 + enable])
            beta = float(args[6 + enable])
            rho = float(args[7 + enable])
            Q = int(args[8 + enable])
            scheme = int(args[9 + enable])
            sites = Sites(filename)
            locations = sites.getLocations()
            graph = Graph(locations, GLPK)
            aco = ACO(iterations, totalAnts, alpha, beta, rho, Q, scheme)
            startTime = time.time()
            path, cost = aco.solveModel(graph)
            runTime = (time.time() - startTime)
            route = sites.generateRoute(path)
            print('cost: {}, runTime: {}, route: {}'.format(cost, runTime, route))
            plot(locations, path)
        except:
            helpMessage()
    
    #solveMultipleModels: It solves the TSP problem using multiple colonies varying its parameters to return the best colony parameters. 
    elif args[1] == 'solveMultipleModels':
        try:
            GLPK = True if args[2] == 'GLPK' else False
            enable = 1 if GLPK == True else 0
            filename = str(args[2 + enable])
            iterationsPerColony = int(args[3 + enable])
            totalAntsAlterations = int(args[4 + enable])
            totalAntsRange = (int(args[5 + enable]),int(args[6 + enable]))
            alphaAlterations = int(args[7 + enable])
            alphaRange = (float(args[8 + enable]),float(args[9 + enable]))
            betaAlterations = int(args[10 + enable])
            betaRange = (float(args[11 + enable]),float(args[12 + enable]))
            rhoAlterations = int(args[13 + enable])
            rhoRange = (float(args[14 + enable]),float(args[15 + enable]))
            QAlterations = int(args[16 + enable])
            QRange = (int(args[17 + enable]),int(args[18 + enable]))
            sites = Sites(filename)
            locations = sites.getLocations()
            graph = Graph(locations, GLPK)
            totalAntsAlterations = randomInteger(totalAntsAlterations, totalAntsRange[0],totalAntsRange[1])
            alphaAlterations = randomFloat(alphaAlterations, alphaRange[0],alphaRange[1])
            betaAlterations = randomFloat(betaAlterations, betaRange[0], betaRange[1])
            rhoAlterations = randomFloat(rhoAlterations, rhoRange[0], rhoRange[1])
            QAlterations = randomInteger(QAlterations, QRange[0], QRange[1])
            schemes = [0,1,2]
            logSize = 10
            bestCosts = [0]*logSize
            bestColonies = [0]*logSize
            bestParameters = [[0]*9]*logSize
            print("iterationsPerColony: {}".format(iterationsPerColony))
            colony = 0
            for totalAntsAlteration in totalAntsAlterations:
                for alphaAlteration in alphaAlterations:
                    for betaAlteration in betaAlterations:
                        for rhoAlteration in rhoAlterations:
                            for QAlteration in QAlterations:
                                for scheme in schemes:
                                    aco = ACO(iterationsPerColony, totalAntsAlteration, alphaAlteration, betaAlteration, rhoAlteration, QAlteration, scheme)
                                    startTime = time.time()
                                    path, cost = aco.solveModel(graph)
                                    runTime = (time.time() - startTime)
                                    if cost < bestCosts[0] or bestCosts[0] == 0:
                                        for i in range(logSize-1,0,-1):
                                            bestColonies[i] = bestColonies[i-1]
                                            bestCosts[i] = bestCosts[i-1]
                                            bestParameters[i] = bestParameters[i-1]
                                        bestColonies[0] = colony
                                        bestCosts[0] = cost
                                        bestParameters[0] = [cost, colony, totalAntsAlteration, alphaAlteration, betaAlteration, rhoAlteration, QAlteration, scheme, runTime]
                                        exportResults(filename, iterationsPerColony, bestParameters)
                                    print("bestCosts: {}".format(bestCosts))
                                    print("bestColonies: {}".format(bestColonies))
                                    
                                    print("cost: {}, colony: {}, totalAnts: {}, alpha: {}, beta: {}, rho: {}, Q: {}, scheme: {}, runTime: {}".format(round(cost,2), colony, totalAntsAlteration, round(alphaAlteration,2), round(betaAlteration,2), round(rhoAlteration,2), QAlteration, scheme, round(runTime,3)))
                                    exportLog(filename, iterationsPerColony, cost, colony, totalAntsAlteration, alphaAlteration, betaAlteration, rhoAlteration, QAlteration, scheme, runTime)
                                    colony += 1
        except:
            helpMessage()
    #plotRoute: It show the Sites on the map and generate its path or route.
    elif args[1] == 'plotRoute':
        try:
            filename = str(args[2])
            route = [int(indexSite) for indexSite in args[3:]]
            sites = Sites(filename)
            locations = sites.getLocations()
            path = sites.generatePath(route)
            plot(locations, path)
        except:
            helpMessage()
    else:
        helpMessage()

def exportLog(filename : str, iterationsPerColony, cost, colony, totalAntsAlteration, alphaAlteration, betaAlteration, rhoAlteration, QAlteration, scheme, runTime):
    if colony == 0:
        with open("./data/{}-LOGx{}.dat".format(filename, iterationsPerColony), "w") as file:
            file.writelines('iterationsPerColony: {}\n'.format(iterationsPerColony))
            file.writelines('cost, colony, totalAnts, alpha, beta, rho, Q, scheme, runTime\n')
    with open("./data/{}-LOGx{}.dat".format(filename, iterationsPerColony), "a") as file:
        line = [str(round(cost,2)), str(colony), str(totalAntsAlteration),str(round(alphaAlteration,2)), str(round(betaAlteration,2)), str(round(rhoAlteration,2)), str(QAlteration), str(scheme), str(round(runTime,3))]
        file.writelines(','.join(line))
        file.writelines('\n')
            
def exportResults(filename : str, iterationsPerColony, bestParameters: list):
    with open("./data/{}-RESULTSx{}.dat".format(filename, iterationsPerColony), "w") as file:
        file.writelines('iterationsPerColony: {}\n'.format(iterationsPerColony))
        file.writelines('cost, colony, totalAnts, alpha, beta, rho, Q, scheme, runTime\n')
        for bestParameter in bestParameters:
            cost , colony, totalAntsAlteration, alphaAlteration, betaAlteration, rhoAlteration, QAlteration, scheme, runTime = bestParameter
            line = [str(round(cost,2)), str(colony), str(totalAntsAlteration),str(round(alphaAlteration,2)), str(round(betaAlteration,2)), str(round(rhoAlteration,2)), str(QAlteration), str(scheme), str(round(runTime,3))]
            file.writelines(','.join(line))
            file.writelines('\n')

def randomInteger(total: int, minimumValue: int, maximumValue: int):
    return sorted([random.randint(minimumValue, maximumValue) for i in range(total)])

def randomFloat(total: int, minimumValue: float, maximumValue: float):
    return sorted([random.uniform(minimumValue, maximumValue) for i in range(total)])

def helpMessage():
    print("HELP COMMANDS\n")
    print("generateSites [filename] [totalSites] [longitudeRangeMin] [longitudeRangeMax] [latitudeRangeMin] [latitudeRangeMax]\n")
    print("generateSites GLPK [filename] [totalSites] [longitudeRangeMin] [longitudeRangeMax] [latitudeRangeMin] [latitudeRangeMax]\n")
    print("solveModel [filename] [iterations] [totalAnts] [alpha] [beta] [rho] [Q] [scheme]\n")
    print("solveMultipleModels [filename] [iterationsPerColony] [totalAntsAlterations] [totalAntsMin] [totalAntsMax] [alphaAlterations] [alphaMin] [alphaMax] [betaAlterations] [betaMin] [betaMax] [rhoAlterations] [rhoMin] [rhoMax] [QAlterations] [QMin] [QMax]\n")
    print("plotRoute [filename] [indexSite0] [indexSite1] [indexSite3] ... [indexSiteN]\n")

if __name__ == '__main__':
    main(sys.argv)
