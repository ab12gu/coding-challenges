## filename: kmeans.py
# by: Abhay Gupta
# date: 23-08-25
#
# 1: Init: Start with 2 points as centroid
# 2. Add new point to nearest centroid
# 3. re-calculate cluster from added point
# 4. end if centroid the same, else repeat step 2 onwards


import random
import matplotlib.pyplot as plt

class Clustering:
    """ Clustering algorithms """


    def dist(self, p1, p2):
        """ euclidean distance """
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(1/2)

    def mean(self, clist):
        """ mean of numbers """
        x = sum(i[0] for i in clist)/len(clist)
        y = sum(i[1] for i in clist)/len(clist)
        return x,y

    def plot(self, alist, blist, a, b):
        """ scatterplot of points """

        # plot points
        x, y = zip(*alist)
        plt.plot(x,y, 'bo')
        x, y = zip(*blist)
        plt.plot(x,y, 'ro')
        
        # plot centroids
        plt.plot(*a, 'bx', markersize=50)
        plt.plot(*b, 'rx', markersize=50)
        plt.show()

    def kmeans(self, points):
        """ find the kmeans of points """

        a = points[0]
        b = points[1]

        while(1):

            c = (a, b)
            alist = []
            blist = []


            for i in points:

                if self.dist(a, i) < self.dist(b, i):
                    alist.append(i)
                else:
                    blist.append(i)

            a = self.mean(alist)
            b = self.mean(blist)


            if c[0] == a and c[1] == b:

                # plot
                self.plot(alist, blist, a, b)
                # centroids
                return c

                        
if __name__ == "__main__":
    # test cases

    points = random.random()
    #print(points)
    
    size = 100
    a = [random.random() for i in range(size)]
    b = [random.random() for i in range(size)]

    points = [(i) for i in zip(a, b)]

    #print("Length: ", size)
    #print("Points: ", points)
    
    centroids = Clustering().kmeans(points)
    print(centroids)


