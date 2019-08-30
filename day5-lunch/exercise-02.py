#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


#df = pd.read_ctab(sys.argv[1], index_col="t_name")

# posit_list = []
# negat_list = []
for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    # protein_region =
    
    if fields[2] == "+":
        promoter_left = int(fields[3])-500
        promoter_right = int(fields[3])+ 500  
        promoter_left = max(promoter_left, 1)
        # posit_list = posit_list.append(promoter_plus)
    else:
        fields[2] == "-"
        promoter_left = int(fields[4])+500
        promoter_right = int(fields[4])- 500 
        promoter_left = max(promoter_left, 1)
         
        
        
        # negat_list = negat_list.append(promoter_minus)
    print(fields[1],promoter_left,promoter_right,fields[5],sep='\t')
# print(posit_list, negat_list)
    




    