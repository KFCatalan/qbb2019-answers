#!/usr/bin/env python3



""""
sage: ./merge_fpkms.py <threshold> <criteria> <ctab_file1> <ctab_file2> ... <ctab_filen>
"""

import sys
import os
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

ctab_dict = {}



ctab = pd.read_csv(sys.argv[1], sep="\t")
name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
name2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name" )

fpkm= { name1 : ctab1.loc[:, "FPKM"],
        name2 : ctab2.loc[:, "FPKM"]}


















