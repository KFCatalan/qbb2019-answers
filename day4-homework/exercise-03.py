#!/usr/bin/env python3

""""
Usage: ./02-timecvourse.py <t_name> <samples.csv> <FPKMs.
Create a timecourse of a given transcript for females
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

def get_fpkms(sample_file,sex_,ctab_dir):
    fpkms = []
    for i, line in enumerate(sample_file):
        if i==0:
            continue
        fields = line.rstrip("\n").split(',')
        sample= fields[0]
        sex = fields[1]
        stage = fields[2]
        if sex != sex_:
            continue
        ctab = os.path.join(ctab_dir,sample,"t_data.ctab")
        df = pd.read_csv(ctab,sep='\t', index_col="t_name")
        fpkms.append(df.loc["FBtr0331261","FPKM"])
    return fpkms  

def sex_choose(ax, fpkms, sex, transcript, color ):
    ax.plot(range(8), fpkms.loc[transcript,:], label=sex, color=color)

t_name = sys.argv[1]
samples = pd.read_csv(sys.argv[2])


fpkms = pd.read_csv(sys.argv[3], index_col="t_name")
fpkms = fpkms.drop(columns= "gene_name")

male = fpkms.iloc[:,:8]
female = fpkms.iloc[:,8:]

male_rep = get_fpkms(open(sys.argv[4]),"male",sys.argv[5])
female_rep = get_fpkms(open(sys.argv[4]),"female",sys.argv[5])

column_names = [0,10,11,12,13,"14A", "14B", "14C", "14D"]
sex_label= ["Male", "Female"]

fig, ax = plt.subplots()

ax.set_xticklabels(column_names, rotation= 90)
sex_choose(ax, male, "male", t_name, "blue")
sex_choose(ax, female, "female", t_name, "red")


ax.plot(range(4,8),male_rep,'x',label="male rep",color='blue')
ax.plot(range(4,8),female_rep,'x',label="female rep",color='red')
plt.legend( loc = "center left",  bbox_to_anchor=(1,.5))
plt.tight_layout()

plt.title("Sxl")
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abundance (RPKM)")

fig.savefig("re_timecourse.png")
plt.close(fig)





