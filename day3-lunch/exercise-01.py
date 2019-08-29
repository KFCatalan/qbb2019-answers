#!/usr/bin/env python3

import sys


f = open(sys.argv[1])
gene_list = []
search_pos = 21378950
search_chr = "3R"

for i, line in enumerate(f):
    # if i == :
    # print(line,type(line))
    if line.startswith("#"):
        continue
    column = line.rstrip("\n").split()
    chrom = column[0]
    types = column[2]
    gene_start = int(column[3])
    gene_stop = int(column[4])
    gene_name = column[13]
    if chrom == "3R":
        continue
    if types == "gene":
        if 'gene_biotype "protein_coding";' in line:
            gene_list.append((gene_start, gene_stop, gene_name))
    print(gene_list)


lo = 0
hi = len(gene_list)-1
mid = 0
number_iterations = 0

while (lo <= hi):
    mid = int((hi+lo) / 2)
    
    number_iterations += 1

    if (search_pos < gene_list[mid][0]):
        gene_list[lo:mid]
        
    elif (search_pos > gene_list[mid][1]):
        lo = gene_list[mid]
        gene_list[mid:hi]

    else:
        #gene_list[mid] spans the search_pos!
        break

print(gene_list[mid])

print(number_iterations)





