import time
import math
import random
import matplotlib.pyplot as plt


inputs = [1, 5, 10, 15, 200, 300, 500, 700, 900, 1000]

time_plot = []
time_plot2 = []
random_coordinate = []
x_value = []
y_value = []
x_clone = []
y_clone = []
time_class = []

class Point:
    def __init__(self, x_init, y_init, value):
        self.x = x_init
        self.y = y_init
        self.value = value

    def get_x(self):
        print(self.x)
        return self.x

    def get_y(self):
        return self.y

    def __repr__(self):
        return "".join(["(", str(self.x), ",", str(self.y), ")"])

    def __str__(self):
        return (self.x, self.y)
        #return "(%s,%s)" % (self.x, self.y)

    def distance(self):
        start = time.time()
        d_istance = []

        while self.value > 0:
            random_coordinate.append((random.randint(100, 100000), random.randint(100, 100000)))
            self.value -= 1

        for x in range(len(random_coordinate)):
            x_value.append(random_coordinate[x][0])

        for y in range(len(random_coordinate)):
            y_value.append(random_coordinate[y][1])

        for copy in x_value:
            x_clone.append(copy)

        for copy2 in y_value:
            y_clone.append(copy2)

        for euclid in range(int(len(x_value) / 2)):
            dist = math.sqrt( ((x_value[0] - x_value[1]) ** 2) + ((y_value[0] - y_value[1]) ** 2))
            d_istance.append(dist)
            x_value.pop(0)
            x_value.pop(0)
            y_value.pop(0)
            y_value.pop(0)

        distance_index = d_istance.index(min(d_istance))

        if distance_index == 0:
            print("The closest coordinate is point 1 and 2")
            print(x_clone[0],y_clone[0],"and",x_clone[1],y_clone[1])
            #print("(%d, %d) and (%d, %d)" % (x_clone[0], y_clone[0], x_clone[1], y_clone[1]))
        else:
            one = (distance_index * 2) + 1
            two = (distance_index * 2) + 2
            ind_one = (distance_index * 2)
            ind_two = (distance_index * 2) + 1
            #print("The closest coordinate is point %d and %d" % (one, two))
            print("The closest coordinate is point", (one, two))
            print((x_clone[ind_one],y_clone[ind_one]),"and",(x_clone[ind_two],y_clone[ind_two]))
            #print("(%d, %d) and (%d, %d)" % (x_clone[ind_one], y_clone[ind_one], x_clone[ind_two], y_clone[ind_two]))
        print("The closest distance between point value is: ", min(d_istance))
        end = time.time()
        #time_class.append(end - start)
        print("Time execution: ", end - start, "s")

# plot_graph(True)
point = Point(10, 10, 100000)
point.distance()