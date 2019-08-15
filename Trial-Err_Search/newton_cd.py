from math import cos

x = 1111.; dx = 3.e-4; eps = 0.002; nmax = 100;

def f(x):
    return 2 * cos(x) - x

for it in range(0, nmax + 1):
    f = f(x)
    if (abs(f) <= eps):
        print("\n Root found, f(root) =", f, ", eps = " , eps)
        break
    print("Iteration # = ", it, " x = ", x, " f(x) = ", f)
    df = (f(x + dx / 2) - f(x - dx / 2)) / dx
    dx = -f / df
    x += dx
