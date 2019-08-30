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
target_2_target_seq= {}
target_name = {}


for ident, tsequence in treader:
    tsequence = tsequence.upper()
    target_2_target_seq[ident] = tsequence #ident is key and qseq is value
    for i in range(0, len(tsequence) -k +1):
        kmer = tsequence[i:i+k]
        if kmer in kmers:
            kmers[kmer].append((i, ident))
        else:
            kmers[kmer] = [(i, ident)]
            
for ident, qsequence in qreader:
    qsequence = qsequence.upper()
    for j in range(0, len(qsequence) -k +1):
        kmer = qsequence[j:j+k]
        if kmer in kmers:
            for i, ident in kmers[kmer]:    # i and ident within kmers[kmer]
                tseq = target_2_target_seq[ident]  #dictionary identity specifically sent to tseq 
                ts = len(tseq)              #length of the tseq
                qs = len(qsequence)         #length of qseq
                extend_right = True         # boolean sent 
          extended_kmer = kmer 
            while True:
                if extend_right:
                    if qsequence[j + k + 1] == tseq[i + k + 1]
                        i += 1
                        j += 1
                        extended_kmer += tseq[i + k + 1]
                    else:
                        extend_right = False
                        
                else:
                    break
                 if ts == (i + k) or tseq == (j + k):
                     extend_right = False
                     #needs a print statement using 3rd dictionary

# extended_kmers.sort


# uniq the match to avoid repeating
# .append the new_kmerq to the seq j + k

                   
    #5 variables needed for exercise #2
    #quesry start = j -1  j+k +1
    #target start = i -1  i+k+1  
    #query seq = qseq
    #target seq= tseq
    # kmer
    
    