import random


def sample_from_straight_line(a_0, a_1, n, sigma):
    x_min = 0.0
    x_max = 10.0

    points = []
    for index in range(0, n):
        x = random.uniform(x_min, x_max)
        y = a_0 + a_1 * x

        mu = 0.0
        y_noisy = y + random.gauss(mu, sigma)

        points.append([x, y_noisy])

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
    sigma = 0.1
    print 'Sampling {:d} points with sigma = {:0.3f} ...'.format(n, sigma)
    points = sample_from_straight_line(a_0, a_1, n, sigma)

    [a_0_hat, a_1_hat] = compute_linear_least_squares_regression(points)
    print 'Computed parameters\na_0 = {:0.3f}, a_1 = {:0.3f}'.format(a_0_hat, a_1_hat)


if __name__ == '__main__':
    main()