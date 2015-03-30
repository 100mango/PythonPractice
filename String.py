#coding=utf-8

#剑指offer第四题：将字符串里的空格替换为%20

def replaceBlank(string):
	return string.replace(' ','%20')

print replaceBlank('hello world')

#leetcode Reverse Words in a String 
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])