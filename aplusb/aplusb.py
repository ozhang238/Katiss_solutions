#!/usr/bin/python
from sys import stdin
#A+B Problem
#Given N integers in the range [-50_000,50_000], how many ways are there to pick three integers ai,aj,ak, such that
#i,j,k are pairwise distinct and ai+aj=ak? Two ways are different if their ordered triples (i,j,k) of indices are different
#Input
#The first line of input consits of a single integer N ( 1 <= N <= 200_000). The next line consits of N space-separated integers a1,a2,...,aN

#Samples
#Input:
#4
#1 2 3 4
#Output :
#4    (1+2=3),(2+1=3)(1+3=4)(3+1=4)
#Input :
#6
#1 1 3 3 4 6
#Output :
#10 ( 1 + 3 = 4 )x8 , (3+3=6)x2

#Naive solution
#i = 0, j = 1,k = 2
#ai+aj=ak
#if a[i]+a[j] == a[k], increment i by 1,
#if i == j, increment j by 1
# if j == k increment k by 1
# else if not match
# if sum > a[k], increase k by 1
# if sum < a[k], increase i by 1, j = i + 1, k = i + 2
#

def main():
    i = 0
    j = 1 
    k = 2
    total = 0
    N = int(stdin.readline())
    numbers = stdin.readline().split(' ')
    numbers = list(map(lambda x:int(x), numbers))
    while ( i < N - 2):
        #print(i,j,k,total)
        sum = numbers[i]+numbers[j]
        if sum == numbers[k]:
            total += 2
            if ( k < N-1):
                k = k + 1
            elif ( j < N -2):
                j = j + 1
                k = j + 1
                if ( k == j):
                    k = j + 1
            else:
                i = i + 1
                j = i + 1
                k = j + 1
        elif sum < numbers[k]:
            if ( j < N -2):
                j = j + 1
                k = j + 1
            else:
                i = i + 1
                j = i + 1
                k = j + 1
        else:
            if ( k < N-1):
                k = k + 1
            else:
                i = i + 1
                j = i + 1
                k = j + 1

    print(total)

if __name__ == "__main__":
    main()