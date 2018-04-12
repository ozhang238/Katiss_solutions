#!/usr/bin/python
import sys

#You are given a sequence, in the form of a string with characters 0,1,and ? only
#  Suppose there are k ?. Then there are 2k ways to replace each ? by a 0 or 1, giving 2k different 
# 0-1 sequences (0-1 sequences are sequences with only zeroes and ones).

#For each 0-1 sequence, define its number of inversions as the minimum number of adjacent swaps
# required to sort the sequence in non-decreasing order. In this problem, the sequence is sorted 
# in non-decreasing order precisely when all the zeroes occur before all the ones. For example,
#  the sequence 11010 has 5 inversions. We can sort it by the following moves: 11010 -> 11001 -> 10101 -> 01101 -> 01011 -> 00111.

#Find the sum of the number of inversions of the 2k sequences, modulo 1000000007 (109+7).

#INPUT
#The first and only line of input contains the input string, consisting of characters 0, 1, and ? only, 
# and the input string has between 1 to 500000 characters, inclusive.

#OUTPUT
#Output an integer indicating the aforementioned number of inversions modulo 1000000007.

#this version of count is SUPER SLOW GOD DAMN IT
#def count(full_count,ones, s):
#    if (len(s) == 0):
#        return full_count
#    if ( s[0] == '1'):
#        return  count(full_count,ones+1,s[1:])
#    if ( s[0] == '0'):
#       return  count(full_count+ones, ones, s[1:])
#
#   return count(full_count+ones,ones, s[1:]) +  count(full_count, ones+1, s[1:])
            
def count(s):
    ones = 0
    branches = 0
    total = 0
    for char in s:
        if (char == '0'):
            total += ones + branches
        elif ( char == '1'):
            ones += 1
        elif ( char == '?'):
            
            total += ones + branches
            ones += 1
            branches += 1
    return total
        

def main():
    #for s in sys.stdin:
    #   print ( count( 0,0,s  ) % 1000000007 )
    for (s,ans) in (  ("11010",5),("???",6),("?0?",3),("????",80) ):
        print ("s: "+s+"\t\tcount(s):"+str(count(s))+"\texp:"+str(ans)+"\t"+ ("PASS" if count(s) == ans else "FAIL") )
        

if __name__ == "__main__":
    main()