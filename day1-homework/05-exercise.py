#!/usr/bin/env python3

#Exercise 5

f = open('SRR072893.sam')
counter = 0
column_5 = 0
for i, line in enumerate( f ):
    if line.startswith("@"):
        continue
    fields = line.split("\t")
    if fields[2] == "*":
        continue
    counter += 1
    column_5 += float(fields[4])
    
AVG = column_5 / counter
    
print (AVG)



