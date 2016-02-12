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
import csv

rownum = 0
colnum = 0
data = []
#data.append([])

with open(sys.argv[1], 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        if rownum == 0:
            header = row
            print header
        else:
            print "Rownumber: %d" % rownum
            data.append([])
            colnum=0
            for col in row:                
                data[rownum-1].append(float(col))
                colnum += 1
                
        rownum += 1
    

data_array = asarray(data)
s = shape(data_array)

# Do some sweet plotting
print "Welcome to SexyPlot, we will be happy to serve you some of the"
print "hottest plots on the market."

ifig = 0
legends = []

while True:
    # Get x-axis
    print "x to plot", header
    user_input = raw_input([":"])
    if user_input == "q":
        quit()
    colnum = 0
    for col in header:
        if user_input in col:
            x = data_array[:,colnum]
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
            leg = col
        colnum += 1

    # Add stuff to plot
    figure(ifig)
    pyplot.plot(x,y)
    legends.append(leg)    

    # Plot?
    print "Plot? y/n"
    user_input = raw_input(["Plot?:"])
    if user_input in "y":
        pyplot.legend(legends)
        pyplot.show()
        legends = []
    elif user_input in "q":
        quit()
    elif user_input == "new":
        pyplot.legend(legends)
        legends = []
        ifig += 1
        figure(ifig)
        

#for x in xrange(1,s[1]):
#    figure(x)
#    pyplot.plot(data_array[:,0],data_array[:,x])
#    pyplot.legend([header[x]],"upper left")
#    
#pyplot.show()

