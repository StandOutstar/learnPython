from lxml import html
import requests

# xpath分析方法
# 1. 手动分析
# 2. chrome生成法,使用插件查看xptah


page = requests.get('http://www.vipjiexi.com/')
# page = requests.get('http://www.jikexueyuan.com/')

print(page.encoding)
# 编码转换 ISO-8859-1 -> utf-8
text = page.text.encode('ISO-8859-1').decode('utf-8')
print(text)

tree = html.fromstring(text)
# 通过绝对路径取文本
head = tree.xpath('/html/body/div[1]/text()')
print(head)

# 相对路径取属性
inputva = tree.xpath('//input[@id="post"]/@value')
print(inputva)

# 相对路径取属性
img = tree.xpath('//img/@src')
print(img)

# 通过附加条件选择节点
head = tree.xpath('/html/body/div[position()<2]/text()')
print(head)
head = tree.xpath('/html/body/div[last()-1]/text()')
print(head)
