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

#leetcode single number
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A): #翻硬币思路，遇到一次就翻一次，则最后只有一个是反面
        result = 0
        for number in A:
            result = result ^ number
        return result
     
#leetcode Single Number II        
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        dictionary = {}
        for number in A:
            if number not in dictionary:
                dictionary[number] = 1
            else:
                dictionary[number] = dictionary[number] + 1
        for number in dictionary:
            if dictionary[number] == 1:
                return number