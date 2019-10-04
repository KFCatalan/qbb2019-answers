#!/usr/bin/env python3


import sys
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

components = open(sys.argv[1])
comp1list = []
comp2list = []

all_data = []
families = set()
for line in components:
    if line.startswith("#"):
        continue
    field = line.rstrip("\n").split()
    comp1 = field[2]
    comp2 = field[3]
    family = field[0]
    comp1list.append(float(field[2]))
    comp2list.append(float(field[3]))
    all_data.append((family, float(comp1), float(comp2)))
    families.add(family)

colors = ['#800000', '#9A6324', '#e6194B', '#808000', '#ffe119', '#469990', '#000075', '#000000', '#f032e6', '#aaffc3', '#a9a9a9']
families = list(families)

fam_color_match = {}
for  i in range(len(families)):
    fam_color_match[families[i]] = colors[i]
    

fig, ax = plt.subplots()

for data_point in all_data:
    ax.scatter(data_point[1], data_point[2], color = fam_color_match[data_point[0]])


plt.title("PCA plot")
plt.xlabel("PCA1")
plt.ylabel("PCA2")
fig.savefig("analysis1.png")
plt.close(fig)

#set = doesnt have repeated values
#all_data = tuple
#family id, x y
#for loop per tuple
#color,x,y (dictionaryt family, color)
