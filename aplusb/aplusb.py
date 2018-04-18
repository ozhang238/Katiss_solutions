#!/usr/bin/python
from sys import stdin
import timeit
import bisect
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


def testvectors():
    test = [    (4,[1,2,3,4], 4),
                (6,[1,1,3,3,4,6], 10 ),
                (8,[1,1,2,2,3,3,4,4],40 ),
                (7,[-5,1,4,9,10,20,21], 6),
                (4,[-4,-3,-2,-1],4),
                (4,[-4,-3,2,1],2),
                (1,[1],0),
                (3,[1,2,3],2),
                (5,[-2,-1,-1,0,1],14)
    ]

    for N,num,exp in test:
        total = (get_total ( N,num ) )
        print("N="+str(N)+" nums="+str(num)+" total="+str(total) +" expected = "+str(exp))
        if ( exp != total ):
            print("FAIL")

setup = '''
import random
import bisect
random.seed('slartibartfast')
s = [random.random() for i in range(160)]
N = len(s)
def get_total(N,num):
    num = sorted(num)
    num_sum = 0
    total = 0
    def search_around(lo,mid,hi,num_sum,num):
        m_lo = mid
        m_hi = mid
        for i in range(mid+1,hi):
            if (num[i] != num_sum):
                break
            m_hi = i
        for i in range(mid-1,lo-1,-1):
            if (num[i] != num_sum):
                break
            m_lo = i
        return m_hi - m_lo + 1
    def bin_search_around(lo,hi,num_sum,num):
        if ( hi == lo ):
            mid = lo
        else:
            mid = lo + bisect.bisect_left( num[lo:hi], num_sum )
        #print(lo,hi,num[lo:hi],num_sum,mid)
        if ( mid < hi and num[mid] == num_sum ):
            return search_around(lo,mid,hi,num_sum,num)
        else:
            return 0

    for i in range(N):
        for j in range(i+1,N):
            num_sum = (num[i]+num[j])
            if ( num_sum <= num[i]): #let's add them, if less then search left, if > than search right
                total += bin_search_around(0,i, num_sum, num  )
            if (num_sum >= num[j]):
                total += bin_search_around(j+1,N, num_sum, num  )
            if ( num_sum >= num[i] and num_sum <= num[j]):
                total += bin_search_around(i+1,j, num_sum, num  )
    return total*2

def get_total_old(N,num):
    num = sorted(num)
    num_sum = 0
    total = 0
    def search_around(lo,mid,hi,num_sum,num):
        m_lo = mid
        m_hi = mid
        for i in range(mid+1,hi):
            if (num[i] != num_sum):
                break
            m_hi = i
        for i in range(mid-1,lo-1,-1):
            if (num[i] != num_sum):
                break
            m_lo = i
        return m_hi - m_lo + 1
    def bin_search_around(lo,hi,num_sum,num):
        if ( hi == lo ):
            mid = lo
        else:
            mid = lo + bisect.bisect_left( num[lo:hi], num_sum )
        if ( mid < hi and num[mid] == num_sum ):
            return search_around(lo,mid,hi,num_sum,num)
        else:
            return 0

    for i in range(N):
        for j in range(i+1,N):
            num_sum = (num[i]+num[j])
            if ( num_sum <= num[i]): #let's add them, if less then search left, if > than search right
                total += bin_search_around(0,i, num_sum, num  )
            if (num_sum >= num[j]):
                total += bin_search_around(j+1,N, num_sum, num  )
            if ( num_sum >= num[i] and num_sum <= num[j]):
                total += bin_search_around(i+1,j, num_sum, num  )
    return total*2

'''
    
def get_total(N,num):
    num = sorted(num)
    num_sum = 0
    total = 0
    def search_around(lo,mid,hi,num_sum,num):
        m_lo = mid
        m_hi = mid
        for i in range(mid+1,hi):
            if (num[i] != num_sum):
                break
            m_hi = i
        for i in range(mid-1,lo-1,-1):
            if (num[i] != num_sum):
                break
            m_lo = i
        return m_hi - m_lo + 1
    def bin_search_around(lo,hi,num_sum,num):
        if ( hi == lo ):
            mid = lo
        else:
            mid = lo + bisect.bisect_left( num[lo:hi], num_sum )
        if ( mid < hi and num[mid] == num_sum ):
            return search_around(lo,mid,hi,num_sum,num)
        else:
            return 0

    for i in range(N):
        for j in range(i+1,N):
            num_sum = (num[i]+num[j])
            if ( num_sum <= num[i]): #let's add them, if less then search left, if > than search right
                total += bin_search_around(0,i, num_sum, num  )
            if (num_sum >= num[j]):
                total += bin_search_around(j+1,N, num_sum, num  )
            if ( num_sum >= num[i] and num_sum <= num[j]):
                total += bin_search_around(i+1,j, num_sum, num  )
    return total*2


def get_num(num_str):
    return list(map(lambda x:int(x),num_str.split(' ') ))

def timing():
    print min(timeit.Timer('a=s[:]; get_total(N,a)',setup=setup).repeat(7,20) )
    print min(timeit.Timer('a=s[:]; get_total_old(N,a)',setup=setup).repeat(7,20) )

def main():
    #testvectors()
    timing()
    #print(get_total( int(stdin.readline()), get_num(stdin.readline())) )

if __name__ == "__main__":
    main()
