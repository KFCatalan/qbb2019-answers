#!/usr/bin/env python3

""""
Usage: ./03-boolean.py <ctab> <chr> <FPKM>

Subset using boolean filters
"""

import sys
import os
import numpy as np
import pandas as pd
import scipy.stats as stats
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
my_data = np.log2(df)
print(df)
print(type(df))


fig, ax = plt.subplots()
ax.scatter( my_data.loc[:, name1], my_data.loc[:, name2], alpha=0.5, c="blue")



plt.title("Merge of scatterplots")
plt.xlabel("log2 FPKM SRR072893")
plt.ylabel("log2 FPKM SRR072894")
fig.savefig("scatter_merge.png")
plt.close(fig)


