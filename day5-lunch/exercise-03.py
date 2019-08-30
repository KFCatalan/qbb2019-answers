#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


our_data = {}
df = pd.read_csv(sys.argv[1], header=None,index_col=0,sep="\t")
# df.columns = ["1","2","3",sys.argv[1],"5"]
our_data[sys.argv[1]] = df.iloc[:,3]



col_names = df.columns.values.tolist()


df = pd.DataFrame(our_data)





goi["sex"], goi["stage"] = goi.index.str.split("_", 1).str
print(goi)


model = sm.formula.ols(formula = "FPKM ~ sex", data = goi)
ols_results = model.fit()

print(ols_results.summary())