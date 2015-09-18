import random


def f(x):
    # f(x) = x^3 + x^2 + x + 1
    return x*x*x + x*x + x + 1.0


def bisection(xl, xu, xr, es, iteration_max):
    iteration = 0
    while True:
        xr_old = xr
        xr = (xl + xu) / 2.0

        if abs(xr) > 1e-4:
            ea = abs((xr - xr_old) / xr)

        print 'iteration: {:02d}\txr = {:0.8f}\tea = {:0.8f}'.format(iteration, xr, ea)

        test = f(xl) * f(xr)
        if test < 0.0:
            xu = xr
        elif test > 0.0:
            xl = xr
        else:
            ea = 0.0

        if ea < es or iteration > iteration_max:
            break

        iteration += 1

    return xr

    
def main():
    # termination criteria
    es = 1e-4
    iteration_max = 100

    # initial interval
    xl = random.uniform(-10.0, 0.0)
    xu = random.uniform(0.0, 10.0)

    # initial solution
    xr = random.uniform(xl, xu)

    print 'xl: {:08f}\txu = {:0.8f}\txr = {:0.8f}'.format(xl, xu, xr)
    bisection(xl, xu, xr, es, iteration_max)


if __name__ == '__main__':
    main()