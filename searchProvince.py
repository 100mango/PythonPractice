#coding=utf-8
import re
text = '''京
津
沪
渝
蒙
新
藏
宁
桂
港
澳
黑
吉
辽
晋
冀
青
鲁
豫
苏
皖
浙
闽
赣
湘
鄂
粤
琼
甘
陕
黔
滇
川'''

provinceArray = ['@\"' + item + '\"' for item in text.split('\n')]
separator = ',' 
newText = separator.join(provinceArray)

print newText

cityCode =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cityCodeArray = re.findall(r'[A-Z]', cityCode)
iOScityCodeArray = ['@\"' + item + '\"' for item in cityCodeArray]
copyText = separator.join(iOScityCodeArray)
print copyText
