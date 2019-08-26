#!/usr/bin/env python3

#Exercise 1
f = open('SRR072893.sam')
counter = 0
for i, line in enumerate( f ):
    if line.startswith("@"):
        continue
    fields = line.split("\t")
    if fields[2] == "*":
        continue
    counter += 1
    
print (counter)





#counts alignments by 1 until end

