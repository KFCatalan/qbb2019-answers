#!/usr/bin/env python3


import sys 
import matplotlib.pyplot as plt


allele_frequency = []

for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    field = line.rstrip("\n").split()
    info = field[7]
    allele_frequency_split = info.split("=")[1]
    allele_frequency_split = allele_frequency_split.split(",")
    
    for number in allele_frequency_split:
        allele_frequency.append(float(number))


fig, ax = plt.subplots()
ax.hist(allele_frequency, bins = 5000)


ax.set_xlabel("Variants")
ax.set_ylabel("Frequency")
ax.set_title("Allele Frequency plot")
plt.tight_layout()
fig.savefig("allele_frequency.png")
plt.close(fig)
