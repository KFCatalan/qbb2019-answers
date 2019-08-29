#!/usr/bin/env python3


from fasta import FASTAReader
import sys

reader = FASTAReader(sys.stdin)
k = int(sys.argv[1])
query= "../day3-afternoon/subset.fa"
q = open(query, 'r')
target= "../day3-homework/droYak2_seq.fa"
t = open(target, 'r')

qreader= FASTAReader(q)
treader= FASTAReader(t)

kmer_list = []
kmers = {}

for ident, sequence in qreader:
    sequence = sequence.upper()
    for i in range(0, len(sequence) -k +1):
        kmer = sequence[i:i+k]
        if kmer in kmers:
            kmers[kmer].append((i, ident))
        else:
            kmers[kmer] = [(i, ident)]
            
for ident, sequence in treader:
    sequence = sequence.upper()
    for i in range(0, len(sequence) -k +1):
        kmer = sequence[i:i+k]
        if kmer in kmers:
            for positionq, identity in kmers[kmer]:
                print(positionq, identity, kmer)
    
    
            # positionq = kmers[kmer][0]
            # print(positionq)
    # for identity in kmers[kmer]:
    #         identity = kmers[kmer[1]]
    