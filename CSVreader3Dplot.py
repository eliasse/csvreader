#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 18:23:06 2015

@author: eliasstrandell
"""
import sys

from numpy import *
from matplotlib import pyplot
from pylab import *
from scipy.optimize import curve_fit
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3D
import csv

rownum = 0
colnum = 0
data = []
#data.append([])

boundary_x = [1000.0,1000.0,1000.0,-1000.0,-1000.0,-1000.0,-1000.0,1000.0]
boundary_y = [1000.0,1000.0,-1000.0,1000.0,-1000.0,-1000.0,1000.0,-1000.0]
boundary_z = [1000.0,-1000.0,1000.0,1000.0,1000.0,-1000.0,-1000.0,-1000.0]

scale = 0.7

for i in range(0,len(boundary_x)):
    boundary_x[i] = boundary_x[i]*scale
    boundary_y[i] = boundary_y[i]*scale
    boundary_z[i] = boundary_z[i]*scale

# Do some sweet plotting
print "Welcome to SexyPlot, we will be happy to serve you some of the"
print "hottest plots on the market."

with open(sys.argv[1], 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        if rownum == 0:
            header = row
            print header
        else:
            #print "Rownumber: %d" % rownum
            data.append([])
            colnum=0
            for col in row:
                data[rownum-1].append(float(col))
                colnum += 1

        rownum += 1


data_array = asarray(data)
s = shape(data_array)


ifig = 0
legends = []

#while True:
# Get x-axis
print "x to plot", header
user_input = raw_input([":"])
if user_input == "q":
    quit()
colnum = 0
for col in header:
    if user_input in col:
        x = data_array[:,colnum]
        legx = col
    colnum += 1

# Get y-axis
print "y to plot", header
user_input = raw_input([":"])
if user_input == "q":
    quit()

colnum = 0
for col in header:
    if user_input in col:
        y = data_array[:,colnum]
        legy = col
    colnum += 1

# Get y-axis
print "z to plot", header
user_input = raw_input([":"])
if user_input == "q":
    quit()

colnum = 0
for col in header:
    if user_input in col:
        z = data_array[:,colnum]
        legz = col
    colnum += 1

# Add stuff to plot
fig = pyplot.figure(dpi=150)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z,c='r')
ax.scatter(boundary_x,boundary_y,boundary_z,marker='^')

#axb = fig.gca(projection='3d')
#linje = Line3D(boundary_x,boundary_y,boundary_z)
#axb.add_line(linje) #Axes3D.
ax.set_xlabel(legx)
ax.set_ylabel(legy)
ax.set_zlabel(legz)

pyplot.show()

    # Plot?
    # print "Plot? y/n"
    # user_input = raw_input(["Plot?:"])
    # if user_input in "y":
    #     pyplot.legend(legends)
    #     pyplot.show()
    #     legends = []
    # elif user_input in "q":
    #     quit()
    # elif user_input == "new":
    #     pyplot.legend(legends)
    #     legends = []
    #     ifig += 1
    #     figure(ifig)


#for x in xrange(1,s[1]):
#    figure(x)
#    pyplot.plot(data_array[:,0],data_array[:,x])
#    pyplot.legend([header[x]],"upper left")
#
#pyplot.show()
