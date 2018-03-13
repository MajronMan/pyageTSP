# coding=utf-8

from matplotlib import pyplot as plt
from pyage.tsp.tsp_city import City


def plot(cities, canvas):
    for (x, y) in cities:
        canvas.plot(x, y, 'ro')
        plt.draw()


def draw(cities, canvas, width, height):
    plt.ion()
    canvas.clear()
    canvas.set_xlim(0, width)
    canvas.set_ylim(0, height)
    plot(cities, canvas)

    n = len(cities)
    (x1, y1) = cities[0]
    for i in xrange(1, n + 1):
        (x2, y2) = cities[i % n]
        canvas.plot([x1, x2], [y1, y2], color='r', linestyle='-', linewidth=0.4)
        (x1, y1) = (x2, y2)
    plt.pause(0.01)
    plt.ioff()
    plt.savefig("fig.png")


def read_cities(filename):
    cities = []
    with open(filename, "r") as input:
        input.readline()  # skip first line
        for line in input:
            name, x, y = line.strip().split(",")
            cities.append(City(name, int(x), int(y)))
    return cities


if __name__ == "__main__":
    width = 1200
    height = 1200
    genotype = [28, 3, 17, 0, 11, 29, 9, 22, 19, 6, 7, 1, 12, 15, 27, 14, 8, 25, 21, 5, 16, 23, 4, 24, 26, 2, 20, 10,
                18, 13]
    filename = "cities.csv"

    cities_list = read_cities(filename)

    fig = plt.figure()
    canvas = fig.add_subplot(111)

    c = [cities_list[i] for i in genotype]
    cities = [(city.x, city.y) for city in c]

    draw(cities, canvas, width, height)