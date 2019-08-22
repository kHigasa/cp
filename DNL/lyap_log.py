from vpython import *

m_min = 3.5; m_max = 4.5; step = 0.25

graph1 = graph(title='Lyapunov coef (blue) for Logistic Map (red)', xtitle = 'm', ytitle = 'x, Lyap', xmax=5.0, xmin=0, ymax=1.0, ymin=-0.6)
func1 = gdots(color=color.red)
func2 = gcurve(color=color.yellow)

for m in arange(m_min, m_max, step):
    y = 0.5
    suma = 0.0
    for i in range(1, 401, 1):
        y = m * y * (1 - y)
    for i in range(402, 601, 1):
        y = m * y * (1 - y)
        func1.plot(pos=(m, y))
        suma = suma + log(abs(m * (1. - 2. * y)))
    func2.plot(pos=(m, suma / 401))
