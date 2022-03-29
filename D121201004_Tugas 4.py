from tabulate import tabulate
from math import e

mxApproximateError = 2

def f(x):
    return 5 - 5 * x - e**(0.5 * x)
def fd(x):
    return (5 + 0.5 * e**(0.5 * x)) * -1

def bisect(xl = 0, xu = 2, es = mxApproximateError):
    data = []
    iter = 0
    xr = 0

    while True:
        xrold = xr
        xr = (xl + xu) / 2
        iter = iter + 1
        if xr != 0:
            ea = (abs(xr - xrold) / xr) * 100

        data.append([iter, xl, round(f(xl), 4), xu, round(f(xu), 4), xr, round(f(xr), 4), " " if iter == 1 else round(ea, 4)])

        test = f(xl) * f(xr)

        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            ea = 0    

        if ea < es:
            break

    head = ["Itteration", "xl", "f(xl)", "xu", "f(xu)", "xr", "f(xr)", "ea(%)"]
    print("\t\t\t\tThe Bisection Method")
    print(tabulate(data, headers=head, tablefmt="github"))
    print("The root of this function with bracket method (bisection) is", xr)


def newtonRaphson(xi = 0.7, es = mxApproximateError):
    data = []
    iter = 0
    xr = 0
    ea = 0
    data.append([iter, xi, " "])

    while True:
        iter = iter + 1
        
        xinew = xi - f(xi)/fd(xi)
        
        ea = abs(xinew - xi) / xinew * 100

        data.append([iter, xinew, round(ea, 4)])

        if ea < es:
            break

    head = ["Itteration", u"x\u1d62", "ea(%)"]
    print("\t\t\t\tThe Newton-Raphson Method")
    print(tabulate(data, headers=head, tablefmt="github"))
    print("The root of this function with The Newton-Raphson Method is", xinew)

def fixedPoint(xiold = 0, xi = 2, es = mxApproximateError):
    iter = 0
    data = []
    data.append([iter, xiold, f(xiold), xi, f(xi), " ", " "])

    while True:
        xinew = xi - (f(xi) * (xiold - xi))/(f(xiold) - f(xi))

        ea = abs(xinew - xi) / xinew * 100

        iter = iter + 1

        data.append([iter, xiold, f(xiold), xi, f(xi), xinew, ea])

        if ea < es:
            break

        xiold, xi, = xi, xinew
        
    head = ["Itteration", u"x\u1d62\u208b\u2081", u"f(x\u1d62\u208b\u2081)", u"x\u1d62", u"f(x\u1d62)", u"x\u1d62\u208a\u2081", "ea(%)"]
    print("\t\t\t\tThe Fixed Point")
    print(tabulate(data, headers=head, tablefmt="github"))
    print("The root of this function with The Fixed-Point Iteration is", xinew)

print("(a). Use a Bracketing method (Bisection), use initial guesses of xl = 0 and xu = 2")
bisect()
print()
print(u"(b). Use the Newton-Raphson method, use an initial guess of x\u1d62 = 0.7")
newtonRaphson()
print()
print(u"(c) Use the Secant method, use initial guesses of x\u1d62\u208b\u2081 = 0 and x\u1d62 = 2")
fixedPoint()