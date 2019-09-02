#!/usr/bin/env python3

""""
Usage: ./03-boolean.py <ctab> <chr> <FPKM>

Subset using boolean filters
"""

import sys
import numpy as np
import pandas as pd
import scipy.stats as stats
import os
import scipy.stats as skew
import matplotlib.pyplot as plt

ctab = pd.read_csv(sys.argv[1], sep="\t")
name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
name2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name" )

fpkm= { name1 : ctab1.loc[:, "FPKM"],
        name2 : ctab2.loc[:, "FPKM"]}

df = pd.DataFrame(fpkm)
df += 1


my_data = np.log(df)
# my_data_new= np.linspace(0,12,100)
# f=np.poly1d(coeff)

# print(df)
# print(type(df))

#numpy polyfit


#x =list(range(1,10,1))

fig, ax = plt.subplots()
ax.scatter(x= my_data.loc[:, str(name1)], y= my_data.loc[:, str(name2)], s=3, alpha=0.5, c="blue")
#ax.plot( my_data, p(x)) 


polyfit = np.polyfit(x= my_data.loc[:,str(name1)], y= my_data.loc[:,str(name2)], deg=1)
xpolyfit= my_data.loc[:,str(name1)]
ypolyfit= (polyfit[0]* xpolyfit) + polyfit[1]
ax.plot(xpolyfit, ypolyfit, c="red")


print(polyfit)


#print (x)

plt.title("Merge of scatterplots")
plt.xlabel("log FPKM SRR072893")
plt.ylabel("log FPKM SRR072894")
fig.savefig("scatter_merge.png")
plt.close(fig)


