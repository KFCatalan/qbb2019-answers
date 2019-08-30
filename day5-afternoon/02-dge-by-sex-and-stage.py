#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy

df = pd.read_csv(sys.argv[1], index_col="t_name")
col_names = df.columns.values.tolist()

def sex_dge(transcript_id):
    goi = pd.DataFrame(df.loc[transcript_id].iloc[1:])
    goi.columns = ["FPKM"]
    
    goi["FPKM"] = pd.to_numeric(goi["FPKM"])
    
    goi["sex"], goi["stage"] = goi.index.str.split("_", 1).str
    #print(goi)

    goi["stage"].replace("14A", "14", inplace = True)
    goi["stage"].replace("14B", "15", inplace = True)
    goi["stage"].replace("14C", "16", inplace = True)
    goi["stage"].replace("14D", "17", inplace = True)

    goi["stage"] =pd.to_numeric(goi["stage"])

    goi["logFPKM"] = np.log(goi["FPKM"]+1)
    
    model = sm.formula.ols(formula = "logFPKM ~ sex + stage", data = goi)
    ols_results = model.fit()
    
    print(ols_results.summary())

    return(transcript_id, ols_results.pvalues[1],ols_results.pvalues[2])
    
print(sex_dge("Btr0302347"))
#   
#ssex_dge("FBtr0302347")
#
# hi_exp_genes = ((df == 0).sum(axis = 1) == 0) #less than or equal to 3 zeros
# # (hi_exp_genes)
#
# hi_df = df.loc[hi_exp_genes, :]
# hi_exp_genes_list = hi_df.index.values.tolist()
#
# results = []
# for transcript in hi_exp_genes_list:
#     results.append(sex_dge(transcript))
#
# results_df = pd.DataFrame(results,
#     columns = ["t_name", "p_val_sex", "p_val_stage"]).sort_values(by = "p_val")
#
# fig, ax = plt.subplots()
# hist = ax.hist(results_df.loc[:,"p_val"])
# fig.savefig("pvalhist_stage4.png")
# plt.close(fig)









