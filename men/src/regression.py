import matplotlib.pyplot as plt
import numpy
import random


def evaluate_straight_line(a_0, a_1, x):
    y = a_0 + a_1 * x
    return y


def sample_from_straight_line(a_0, a_1, n, sigma, x_min, x_max):
    points = numpy.empty([n, 2])
    index = 0
    while index < n:
        x = random.uniform(x_min, x_max)
        y = evaluate_straight_line(a_0, a_1, x)

        mu = 0.0
        y_noisy = y + random.gauss(mu, sigma)

        points[index, :] = [x, y_noisy]

        index += 1

    return points


def compute_linear_least_squares_regression(points):
    sum_x = 0.0
    sum_y = 0.0
    sum_xx = 0.0
    sum_xy = 0.0
    for point in points:
        [x, y] = point
        # y = point[1]

        sum_x += x
        sum_y += y
        sum_xx += x * x
        sum_xy += x * y

    n = len(points)

    mu_x = sum_x / n
    mu_y = sum_y / n

    a_1 = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
    a_0 = mu_y - a_1 * mu_x

    return [a_0, a_1]


def main():
    a_0 = 0.0
    a_1 = 1.0
    print 'True parameters:\na_0 = {:0.3f}, a_1 = {:0.3f}'.format(a_0, a_1)

    n = 10
    sigma = 0.0
    x_min = 0.0
    x_max = 10.0
    print 'Sampling {:d} points with sigma = {:0.3f} in the interval [{:0.3f}, {:0.3f}] ...'.format(n, sigma, x_min, x_max)
    points = sample_from_straight_line(a_0, a_1, n, sigma, x_min, x_max)

    [a_0_hat, a_1_hat] = compute_linear_least_squares_regression(points)
    print 'Computed parameters\na_0 = {:0.3f}, a_1 = {:0.3f}'.format(a_0_hat, a_1_hat)

    # plot data
    y_min = evaluate_straight_line(a_0, a_1, x_min)
    y_max = evaluate_straight_line(a_0, a_1, x_max)
    plt.plot([x_min, x_max], [y_min, y_max], linewidth=7, label='True')

    plt.plot(points[:,0], points[:,1], 'o', markersize=12, label='Observed')

    y_min_hat = evaluate_straight_line(a_0_hat, a_1_hat, x_min)
    y_max_hat = evaluate_straight_line(a_0_hat, a_1_hat, x_max)
    plt.plot([x_min, x_max], [y_min_hat, y_max_hat], 'r', linewidth=5, linestyle='--', label='Approximated')

    plt.legend(loc='lower right')

    plt.show()


if __name__ == '__main__':
    main()