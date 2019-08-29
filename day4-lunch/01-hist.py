#!/usr/bin/env python3

""""
Usage: ./01-hist.py
Plot FPKM
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

fpkms = []
for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields  = line.rstrip("\n").split("\t")
    if float(fields[11]) > 0:
        fpkms.append( float(fields[11]))

print(len(fpkms))

my_data = np.log2(fpkms)
    
mu = float(sys.argv[2])    #4.3
sigma = float(sys.argv[3])      #1.9



x =np.linspace(- 15, 15, 100)  
y =stats.norm.pdf(x, mu, sigma)
print(y)
print(type(y))

yskew =stats.skewnorm.pdf(x,float(sys.argv[4]), loc=mu, scale=sigma) # (x,-.45, loc=mu, scale=sigma)
print(y)
print(type(y))    
    
    
fig, ax = plt.subplots()
ax.hist( my_data, bins=100, density = True)
ax.plot( x, y, color="red")
ax.plot(x, yskew, color="black")
fig.savefig( "fpkms.png")
plt.close(fig)
plt.title("Histogram of FPKMS")
plt.xlabel("log2 FPKM value")
plt.ylabel("Frequency")










