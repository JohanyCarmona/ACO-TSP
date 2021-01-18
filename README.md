# ACO-TSP
Solve TSP using Ant Colony Optimization in Python 3

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
