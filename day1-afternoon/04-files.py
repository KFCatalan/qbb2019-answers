#!/usr/bin/env python3

import sys

if len(sys.argv ) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

for i, line in enumerate( f ):
    #remove newline character
    line = line.rstrip("\n")
    #skip comment lines
    if line.startswith("#"):
        continue
    #split into fields
    fields = line.split("\t")
        
    if fields[2] == "gene": 
        print(fields[8])     
        print (fields[2], int (fields[4]) - int(fields[3]))





#for line in f:
  #  line = line.rstrip("\n")
  #  print(line)
    
#counter = 0
#while True:
  #  if counter > 10:
  #     break
  #  line = f.readline(.rstrip("\n"))
  #  print(line)
  #  counter += 1



#for i, line in enumerate(f):
#    line = line.rstrip("\n")
#    print( line)
#    if i >= 10:
#        break
    
    
    