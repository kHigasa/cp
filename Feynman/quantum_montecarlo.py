from vpython import *
from numpy import zeros

N = 100; Nsteps = 101;  xscale = 10.                 # Initialize
path = zeros([Nsteps], float);  prob = zeros([Nsteps], float)

trajec = graph(width = 300,height=500, title='Spacetime Paths')
trplot = curve(y = range(0, 100), color=color.magenta)

def PlotAxes():                                       # Axis
   trax = curve(pos=[(-97,-100),(100,-100)],colo =color.cyan)
   label(pos = (0,-110),  text = '0', box = 0, display = trajec)
   label(pos = (60,-110), text = 'x', box = 0, display = trajec) 
def WaveFunctionAxes():                     # Axes for probability
   wvfax=curve(pos =[(-600,-155),(800,-155)],color=color.cyan)
   curve(pos = [(0,-150), (0,400)], color=color.cyan) 
   label(pos = (-80,450), text='Probability', box = 0, display = wvgraph)
   label(pos = (600,-220), text='x', box=0, display=wvgraph)
   label(pos = (0,-220), text='0', box=0, display=wvgraph)
def Energy(path):                                   # HO Energy
    sums = 0.
    for i in range(0,N-2):sums += (path[i+1]-path[i])*(path[i+1]-path[i])
    sums += path[i+1]*path[i+1]; 
    return sums 
def PlotPath(path):                               # Plot trajectory
   for j in range (0, N):
       trplot.x[j] = 20*path[j]
       trplot.y[j] = 2*j - 100   
def PlotWF(prob):                                      # Plot prob
    for i in range (0, 100):
       wvplot.color = color.yellow
       wvplot.x[i] = 8*i - 400                         # Center fig

wvgraph = graph(x=340,y=150,width=500,height=300, title='Ground State')
wvplot = curve(x = range(0, 100))
wvfax = curve(color = color.cyan)
PlotAxes();  WaveFunctionAxes()                       # Plot axes
oldE = Energy(path)
while True:                                 # Pick random element
    rate(10)                                     # Slow paintings
    element = int(N*random.random() )               # Metropolis
    change = 2.0*(random.random() - 0.5)    
    path[element] += change                        # Change path
    newE = Energy(path);                             # Find new E
    if  newE > oldE and math.exp( - newE + oldE)<= random.random():
          path[element] -= change                     # Reject
          PlotPath(path)                     # Plot trajectory
    elem = int(path[element]*16 + 50)    # if path = 0, elem = 50
    if elem < 0: elem = 0,                     
    if elem > 100:  elem = 100                 # If exceed max
    prob[elem] += 1                     # increase probability
    PlotWF(prob)
    oldE = newE
