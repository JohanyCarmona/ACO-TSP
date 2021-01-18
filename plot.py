import operator
import matplotlib.pyplot as plt

def plot(sites, path: list):
    x = []
    y = []
    
    for site in sites:
        x.append(site[0])
        y.append(site[1])
   
    plt.plot(x, y, 'ko')
    plt.plot(x[path[0]],y[path[0]],'bo')
    plt.plot(x[path[-1]],y[path[-1]],'ro')
    
    for step in range(-1,len(path)-1):
        i = path[step]
        j = path[step + 1]
        #Trace the graph route.
        plt.arrow(x[i], y[i], x[j] - x[i], y[j] - y[i], color = 'k', length_includes_head=False)
    plt.xlim(delimit(min(x),max(x)))
    plt.ylim(delimit(min(y),max(y)))
    plt.grid()
    plt.show()
    
def delimit(minimum: float, maximum: float, border: float = 0.1):
    delta = (maximum - minimum) * border
    return (minimum - delta, maximum + delta)
