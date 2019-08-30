#!/usr/bin/env python3

"""
Usage: ./00-metadata.py <metadata> <ctab_dir>

<ctab_dir> e.g. ~./qbb2019-answers/results/stringtie

Create all.csv with FPKMs

    t_name, gemne_name, sample1, ..., samplen
"""


import sys
import os
import pandas as pd

metadata = sys.argv[1]
ctab_dir = sys.argv[2]

fpkms = {}
column = {}

for i, line in enumerate(open(metadata)):
    if i == 0:
        continue
    column = line.rstrip("\n").split(",")
    srr_id = column[0]
    new_sample = column[1] + "_" + column[2]
    ctab_path = os.path.join(ctab_dir, srr_id,
                                "t_data.ctab")
    #print(ctab_path)
    
    df = pd.read_csv(ctab_path, sep="\t",
                        index_col="t_name")
    fpkms["gene_name"] = df.loc[:,"gene_name"]
    fpkms[new_sample] = df.loc[:,"FPKM"]
        
print(new_sample)


df_fpkms = pd.DataFrame(fpkms)
print(df_fpkms.describe())
pd.DataFrame.to_csv(df_fpkms, "re_all.csv")
