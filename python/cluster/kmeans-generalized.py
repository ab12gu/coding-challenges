#!/usr/bin/env python

## filename: kmeans.py
# by: Abhay Gupta
# date: 23-08-25
#
# 1: Init: Start with 2 points as centroid
# 2. Add new point to nearest centroid
# 3. re-calculate cluster after all points are added
# 4. end if centroid the same, else repeat step 2 onwards

import random
import matplotlib.pyplot as plt

class Clustering:
    """ Clustering algorithms """

    def dist(self, p1, p2):
        """ euclidean distance """
        return sum((i-j)**2 for i,j in zip(p1,p2))**(1/2)

    def mean(self, clist):
        """ mean of numbers """
        return (*(sum(i)/len(clist) for i in zip(*clist)),)


    def plot(self, clusters, centroids, k):
        """ scatterplot of points """
        num_of_colors = [i/k for i in list(range(k))]
        colors = iter(plt.cm.rainbow(num_of_colors))

        # plot each point in each cluster and each centroid
        while(clusters):
            color = next(colors)
            plt.plot(*zip(*clusters.pop()), c=color, marker='o', linestyle='None')
            plt.plot(*centroids.pop(), c=color, marker='x', markersize=50)
       
        plt.show()

    def kmeans(self, points, k):
        """ find the centroids of points using kmeans"""

        new_centroids = points[:k]
        num_of_coords = len(points[0])

        while(1):

            alist, blist = [], []
            centroids = new_centroids
            clusters = [[] for _ in range(k)]
            
            # find the closet centroid for each point
            for i in points:
                shortest_dist = self.dist(centroids[0], i)
                cluster = 0
                
                for c, j in enumerate(centroids[1:]):
                    distance = self.dist(j, i)
                    if distance < shortest_dist:
                        shortest_dist = distance
                        cluster = c + 1
                
                # add point to closest centroid
                clusters[cluster].append(i)

            # calculate centroid of each cluster
            new_centroids = [self.mean(i) for i in clusters]
            
            # check if old centroids match new centroids
            if centroids == new_centroids:

                # plot if data is 2D
                if num_of_coords == 2:
                    self.plot(clusters, centroids, k)
                return centroids

if __name__ == "__main__":
    # test cases

    # random: range 0 -> 1
    points = random.random()
    #print(points)
    
    num_of_points = 100
    num_of_coords = 2
    k = 6

    #num_of_points = int(input("Enter # of points: ") or 100)
    points =  [[random.random() for _ in range(num_of_coords)] for _ in range(num_of_points)]
    #print("Points: ", points)
    
    centroids = Clustering().kmeans(points, k)
    print(centroids)


