#!/usr/bin/env python3

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
name2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name" )

fpkm= { name1 : ctab1.loc[:, "FPKM"],
        name2 : ctab2.loc[:, "FPKM"]}
df = pd.DataFrame(fpkm)
df += 1

r= df.loc[:,name2]
g= df.loc[:,name1]
y= np.log2(r/g)       #y = a
x= 0.5 * np.log2(r*g) #x= m

fig, ax = plt.subplots()
plt.title("Male and Female FPKMs")
ax.set_xlabel("logFPKM")
ax.set_ylabel("Frequency")

ax.scatter(x, y, s=3, alpha=0.5)
fig.savefig("ma_plot.png")
plt.close(fig)

