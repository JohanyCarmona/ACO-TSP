# ACO-TSP
Ant Colony Optimization (ACO) contains the Metaheuristic Python Model in charge of apply diversification and intensifications techniques to obtain the best solution on the Travelling Salesman Problem (TSP).

TSP is an NP-hard problem in combinatorial optimization, important in theoretical computer science and operations research and ask the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?"

## HELP COMMANDS
Bash Commands for the model.

#### python3 main.py generateSites [filename] [totalSites] [longitudeRangeMin] [longitudeRangeMax] [latitudeRangeMin] [latitudeRangeMax]

It generates a file with a randomly set of Sites according the range specified by user.

#### python3 main.py generateSites GLPK [filename] [totalSites] [longitudeRangeMin] [longitudeRangeMax] [latitudeRangeMin] [latitudeRangeMax]

It generates two files: normal data file and GLPK data file with a randomly set of Sites according the range specified by user.

#### python3 main.py solveModel [filename] [iterations] [totalAnts] [alpha] [beta] [rho] [Q] [scheme]

It solves the TSP problem using Ant Colony Optimization according the ACO parameters gived by user.

#### python3 main.py solveMultipleModels [filename] [iterationsPerColony] [totalAntsAlterations] [totalAntsMin] [totalAntsMax] [alphaAlterations] [alphaMin] [alphaMax] [betaAlterations] [betaMin] [betaMax] [rhoAlterations] [rhoMin] [rhoMax] [QAlterations] [QMin] [QMax]

It solves the TSP problem using multiple colonies varying its parameters to return the best colony parameters. 

#### python3 main.py plotRoute [filename] [indexSite0] [indexSite1] [indexSite3] ... [indexSiteN]

It show the Sites on the map and generate its path or route.
