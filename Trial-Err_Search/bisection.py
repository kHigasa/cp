from vpython import *
eps = 1e-3; nmax = 100; a = 0.0; b = 7.0

def f(x):
    return 2 * cos(x) - x

def Bisection(xminus, xplus, nmax, eps):
   for it in range(0, nmax):
       x = (xplus +  xminus) / 2.
       print(" it =", it, " x = ", x, " f(x) =", f(x))
       if (f(xplus) * f(x) > 0.):
           xplus = x
       else:
           xminus = x
       if (abs(f(x)) < eps):
          print("\n Root found with precision eps = ", eps)
          break
       if (it == nmax - 1):
           print ("\n No root after N iterations\n")
   return x

root = Bisection(a, b, nmax, eps)
print(" Root =", root)
