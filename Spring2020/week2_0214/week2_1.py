#!/usr/bin/env python3

"""
Perform Needleman-Wunsch global alignment of two nucleotide sequences.
"""
import sys
import numpy


# note initialize first row and column and fill in the reamining rows and columns 
def sigma(nt_s, nt_t):
  # HoxD70 matrix of Chiaromonte, Yap, Miller 2002,
  #                   A     C     G     T
  sigma_score = [ [   91, -114,  -31, -123 ],
                  [ -114,  100, -125,  -31 ],
                  [  -31, -125,  100, -114 ],
                  [ -123,  -31, -114,   91 ] ]
  nucleotide = ["A","C","G","T"] 
  nts = nt_s, nt_t
  for nt1 in enumerate(nucleotide):
    for nt2 in enumerate(nucleotide):
      indx = nt1[0],nt2[0]
      nt_pair = nt1[1],nt2[1]
      if nts != nt_pair:
        continue
      elif nts == nt_pair:
        pos = indx
        score = sigma_score[pos[0]][pos[1]]
        return score
gap = 300


def compute_matrix( s, t ):
  m = len(s)
  n = len(t)
  dp_matrix = numpy.zeros( (m+1 , n+1), float ) # for original score matrix
  tb_matrix = numpy.zeros( (m+1 , n+1), int ) # for traceback

  #Initialization
  for i in range(m+1):
    dp_matrix[i][0] = (-gap) * i
  for j in range(n+1):
    dp_matrix[0][j] = (-gap) * j

  #Fill the matrix
  for i in range(1 , m+1):
    for j in range(1, n+1):
      v = dp_matrix[i][j-1] - gap
      h = dp_matrix[i-1][j] - gap
      d = dp_matrix[i-1][j-1] + sigma(s[i-1],t[j-1])
      
      #value from sigma matrix, define a function that brings paring score from sigma matrix
      dp_matrix[i][j] = max(v,h,d)
      # dp_matrix is done!!

      #Now build traceback matrix (tb_matrix)
      #Give each direction a corresponding number from 1 to 3 
      if dp_matrix[i][j] == d: # diagonal --> match or mismatch
        tb_matrix[i][j] = 1
      elif dp_matrix[i][j] == h: #
        tb_matrix[i][j] = 2
      elif dp_matrix[i][j] == v: #
        tb_matrix[i][j] = 3
      # tb_matrix is done!!
  #print dp_matrix
  #print tb_matrix
  return dp_matrix, tb_matrix
def print_alignment( dp_matrix, tb_matrix, s, t ):
  # Now tracing back
  align1 = ""
  align2 = ""
  mut = ""
  i = len(s)
  j = len(t)
  # Redirect i and j to the last nt of each sequence, start tracing back from the bottom of the matrix
  align_score = dp_matrix[i][j]
  while i > 0 and j > 0:
    if tb_matrix[i][j] == 1: # diagonal --> match or mismatch
      align1 += s[i-1]
      align2 += t[j-1]
      if s[i-1] == t[j-1]:
        mut += s[i-1]
      elif s[i-1] != t[j-1]:
        mut += "X"
      i -= 1
      j -= 1
    elif tb_matrix[i][j] == 2: # horizontal
      align1 += s[i-1]
      align2 += "-"
      mut += "-"
      i -= 1
    elif tb_matrix[i][j] == 3: # vertical
      align1 += "-"
      align2 += t[j-1]
      mut += "-" 
      j -= 1
  align1 = align1[::-1]
  align2 = align2[::-1]
  print ("Gap:" + "\n" + str(gap) + "\n")
  print ("Alignment 1:" + "\n" + align1 + "\n") 
  print ("Alignment 2:" + "\n" + align2 + "\n")
  print ("Mismatched sites(*):" + "\n" + mut + "\n") 
  print ("Score: " + "\n" + str(align_score))
def main():
    s = open(sys.argv[1]).read().strip()
    t = open(sys.argv[2]).read().strip()
    dp_matrix, tb_matrix = compute_matrix( s, t )
    print_alignment( dp_matrix, tb_matrix, s, t )
if __name__ == "__main__":
    main()

