#coding=utf8
#Number of 1 Bits
#Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
#For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

#一个事实：把一个整数减去1，再和原整数做与运算，会把该整数最右边的一个1变成0
#一个整数的二进制表示多少个1,就可以做多少次这样的操作

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
    	count = 0
    	while n != 0:
    		count = count + 1
    		n = n & (n-1)
    	return count