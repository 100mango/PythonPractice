#coding=utf-8

#剑指offer第四题：将字符串里的空格替换为%20

def replaceBlank(string):
	return string.replace(' ','%20')

print replaceBlank('hello world')