#!/usr/bin/env python3

""""
Usage: ./01-boxplot.py <gene_name> <FPKMs.csv>

Boxplot all trasnscripts for a given gene
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

gene_name = sys.argv[1]
fpkm_file = sys.argv[2]

df= pd.read_csv(fpkm_file, index_col="t_name")

goi = df.loc[:,"gene_name"] == gene_name
# goi = df.iloc[:, 0] == gene_name  


fpkms = df.drop(columns="gene_name")
#print(fpkms.loc[goi,:])
male = fpkms.iloc[:,:8]
female = fpkms.iloc[:,8:]

fig, ax= plt.subplots(2)
ax[0].boxplot(male.loc[goi,:].T)
ax[1].boxplot(female.loc[goi,:].T)

column_names = fpkms.columns
ax[0].set_xticklabels(column_names[:8], rotation= 30)
ax[1].set_xticklabels(column_names[8:], rotation= 30)



plt.title("Male and Female FPKMs")
ax[0].set_xlabel("Sample name")
ax[0].set_ylabel("FPKM values")
ax[1].set_xlabel("Sample name")
ax[1].set_ylabel("FPKM values")
plt.tight_layout()

fig.savefig("boxplot.png")
plt.close(fig)


