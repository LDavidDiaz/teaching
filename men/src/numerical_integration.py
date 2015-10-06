import matplotlib.pyplot
import numpy


def f(x):
    return 1e-2 * x**3 - 2e-1 * x**2 + 1e0 * x + 1


def plot_function(a, b):
    x = numpy.arange(a, b, (b - a) / 100.0)
    matplotlib.pyplot.plot(x, f(x))
    matplotlib.pyplot.show()


def trapezoidal_rule(a, b):
    return (b - a) * (f(a) + f(b)) / 2.0


def trapezoidal_multiple_rule(a, b, n):
    delta = (b - a) / float(n - 1)

    sum = f(a)
    index = 1
    while index < n - 1:
        xi = a + index * delta
        sum += 2 * f(xi)
        index += 1
    sum += f(b)

    return delta * sum / 2.0


def main():
    a = 0
    b = 10
    plot_function(a, b)

    area = trapezoidal_rule(a, b)
    print 'Area using the trapezoidal rule: {:0.3f}'.format(area)

    areas = []
    n_range = range(2, 128, 2)
    for n in n_range:
        area = trapezoidal_multiple_rule(a, b, n)
        print 'Area using the multiple trapezoidal rule: {:0.3f} with {:d} elements'.format(area, n)
        areas.append(area)

    matplotlib.pyplot.plot(n_range, areas)
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
