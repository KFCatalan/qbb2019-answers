#!/usr/bin/env python3

""""
Usage: ./03-boolean.py <ctab> <chr> <FPKM>

Subset using boolean filters
"""

import sys
import os
import pandas as pd

name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")

# fpkm= { "sample1" : [1,2,3],
#          "sample2" : [4,5,6]}
#

name2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name" )

fpkm= { name1 : ctab1.loc[:, "FPKM"],
        name2 : ctab2.loc[:, "FPKM"]}
df = pd.DataFrame(fpkm)

print(df)
print(type(df))


