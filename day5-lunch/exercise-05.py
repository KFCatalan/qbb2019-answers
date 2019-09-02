#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


ctab= pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")


H3K4me1 = pd.read_csv(sys.argv[2], sep="\t", header = None, names= ["t_name", "size", "covered", "sum", "mean_zero", "mean"], index_col="t_name")
H3K4me3 = pd.read_csv(sys.argv[3], sep="\t", header = None, names= ["t_name", "size", "covered", "sum", "mean_zero", "mean"], index_col="t_name")
H3K9me1 = pd.read_csv(sys.argv[4], sep="\t", header = None, names= ["t_name", "size", "covered", "sum", "mean_zero", "mean"], index_col="t_name")

# FPKM for ctab file, mean for tab file
#df = histone of interest
df = pd.DataFrame(np.log(ctab["FPKM"]+ 1))


#histone modification 
df["H3K4me1"] = H3K4me1["mean"]
df["H3K4me3"] = H3K4me3["mean"]
df["H3K9me1"] = H3K9me1["mean"]


model = sm.formula.ols(formula = "FPKM ~ H3K4me1 + H3K4me3 + H3K9me1", data = df)
ols_results = model.fit()

print(ols_results.summary())








fig, ax = plt.subplots()
ax.hist([ols_results.resid], bins= 1000, range= (-10, 10))
ax.set_xlabel("Residual")
ax.set_ylabel("Frequency")
fig.tight_layout()
plt.title("linear Regression of Residuals")
fig.savefig("re_linear_regression.png")
plt.close()

