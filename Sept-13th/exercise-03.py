#!/usr/bin/env python3


import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm



y_values = []
x_values = []


arg1 = open((sys.argv[1]))

for line in arg1: 
    if line.startswith("#"):
        continue
    column = line.rstrip("\n").split("\t")
    for i in range(int(column[5]) - int(column[4]) ):
        x_values.append(int(column[9]) + i)
        y_values.append(int(column[4]) + i)





fig, ax = plt.subplots()
plt.title("Contigs vs references")
ax.scatter(x_values, y_values)


ax.set_xlabel("Total length of contigs")
ax.set_ylabel("Length of reference")

ax.scatter(x_values, y_values)
fig.savefig("reference_spades_contig.png")
plt.close(fig)