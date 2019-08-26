#!/usr/bin/env python3

#Exercise 6

List_base = range(10000, 20000)


f = open('SRR072893.sam')
counter = 0
for i, line in enumerate( f ):
    if line.startswith("@"):
        continue
    fields = line.split("\t")
    if fields[2] == "*":
        continue
    if fields[2] != "2L":
        continue
    if int(fields[3]) >= 10000 and int(fields[3])<= 20000:
            counter += 1
    
print (counter)


