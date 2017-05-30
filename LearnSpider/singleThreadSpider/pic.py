import requests

r = requests.get('http://iflv9.afreecatv.com/AFFLV/03/7/45/9_03_1495952609691177_2147483647_L.jpg')

with open('1.jpg', 'wb') as f:
    f.write(r.content)
