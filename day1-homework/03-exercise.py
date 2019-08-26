#!/usr/bin/env python3

#Exercise 3

f = open('SRR072893.sam')
counter = 0
for i, line in enumerate( f ):
    if line.startswith("@"):
        continue
    fields = line.split("\t")
    if fields[2] == "*":
        continue
    if "NM:i:0" in line:
        if "NH:i:1" in line:
            counter += 1
    
print (counter)


