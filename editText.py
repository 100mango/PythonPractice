# coding=utf-8
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
# print newText

cityCode = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cityCodeArray = re.findall(r'[A-Z]', cityCode)
iOScityCodeArray = ['@\"' + item + '\"' for item in cityCodeArray]
copyText = separator.join(iOScityCodeArray)
# print copyText

cityNames = '''北京|上海|广州|深圳|天津|西安|福州|重庆|杭州|宁波|无锡|南京|合肥|武汉|成都|青岛|厦门|大连|沈阳|长沙|郑州|石家庄|苏州|淄博|南通|南昌|蚌埠|常州|大庆|东莞|佛山|桂林|海口|葫芦岛|济南|焦作|锦州|南宁|太原|芜湖|新乡|烟台|哈尔滨|廊坊|贵阳|珠海|齐齐哈尔|泉州|三亚|温州|中山|昆明|九江|长春|汕头|徐州|扬州|唐山|秦皇岛|邯郸|邢台|张家口|承德|沧州|衡水|大同|阳泉|长治|晋城|朔州|晋中|运城|忻州|临汾|呼和浩特|包头|乌海|赤峰|通辽|鄂尔多斯|呼伦贝尔|巴彦淖尔|乌兰察布|兴安盟|鞍山|抚顺|本溪|丹东|营口|阜新|辽阳|盘锦|铁岭|朝阳|吉林|四平|辽源|通化|松原|白城|延边|鸡西|佳木斯|牡丹江|绥化|连云港|淮安|盐城|镇江|泰州|宿迁|嘉兴|湖州|绍兴|金华|衢州|舟山|台州|丽水|马鞍山|淮北|铜陵|黄山|滁州|阜阳|宿州|巢湖|六安|宣城|莆田|三明|漳州|龙岩|宁德|萍乡|赣州|宜春|上饶|枣庄|东营|潍坊|济宁|泰安|威海|莱芜|临沂|德州|聊城|滨州|菏泽|开封|洛阳|安阳|鹤壁|濮阳|许昌|漯河|三门峡|南阳|商丘|信阳|周口|驻马店|济源|黄石|宜昌|襄阳|鄂州|荆门|孝感|荆州|黄冈|咸宁|随州|恩施|株洲|衡阳|岳阳|常德|益阳|怀化|娄底|韶关|江门|湛江|肇庆|惠州|梅州|河源|阳江|清远|潮州|揭阳|柳州|梧州|北海|钦州|贵港|玉林|贺州|来宾|自贡|攀枝花|遂宁|乐山|南充|眉山|达州|资阳|凉山|六盘水|遵义|安顺|铜仁|黔东南|曲靖|玉溪|丽江|红河|大理|咸阳|渭南|延安|汉中|兰州|白银|天水|平凉|西宁|海东|银川|乌鲁木齐|昌吉|昆山|江阴|义乌|顺德|石河子|仙桃|峨眉山|琼海|张家港|晋江|从化|常熟|海宁|桐乡|迁安|丹阳|太仓|吴江|靖江|石狮|武安|溧阳|慈溪|长兴|兖州|宜兴|东阳|上虞|温岭|永康|余姚|金坛|临海|福清|长乐|章丘|阳朔|德清|诸暨|瑞安|乐清|惠东|凯里|增城|仁怀|兰溪|大丰|东台|嘉善|安吉|当阳|龙口|邳州|枣阳|寿光|青州|荣成|文登|乳山|启东|如皋|开平|台山|鹤山|桦甸|海城|曲阜|邹平|耒阳|江山|嵊泗|宁海|乐昌|英德|句容|伊川|兴化|泰兴|海门|宁乡|高邮|仪征|新泰|平湖|湘阴|诸城|昌邑|偃师|莱州|嵊州|沭阳|射阳|滨海|响水|阜宁|建湖|临清|三河|东港|奉化|广饶|临安|辛集|晋州|肥城|普宁|南沙|新沂|滕州|潜江|庄河|扬中|莱阳|兴宁|澳门|香港
'''
cityArray = ['@\"' + item + '\"' for item in cityNames.split('|')]
cityText = separator.join(cityArray)
# print cityText

points = '''"say1"：[16，84，18.1，80.6}
"say2"：{13.7，81.3，16.6，80.6}
"say3"：{14.2，83.3，18.2，80.2}
"call1"：{20，71.2，27.3，78.7}
"call2"：{17.8，79.8，18.9，84.6}
"call3"：{28，74.2，29.6，71.1}
"aside1"：{8，92，12.1，87.9}
"think1"：{15.8，74.3，26.2，77.7}
"think2"：{12.7，69.2，24.7，77.6}
"think3"：{22，78，22，78} '''

points = points.replace('{', '[')
points = points.replace('}', ']')
points = points.replace('：', ':')
points = points.replace('，', ',')
points = separator.join(points.split('\n'))

print points
