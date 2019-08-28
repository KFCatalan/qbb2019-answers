#!/usr/bin/env python3

import sys
import numpy
import scipy.stats

f = open('exercise_01_output', 'w')
for i, line in enumerate(sys.stdin):
    columns = line.rstrip("\n").split()
    for column in columns[:3]:
        if "DROME" in column:
            if len(columns) < 4:
                continue
            #print(columns[3], columns[1],  sep='\t')
            f.write(columns[-1] + "\t" + columns[-2] + "\n")
            
            # f.write(last, second to last)
