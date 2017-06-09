import requests


def response_hook(response, *args, **kwargs):
    print(response.status_code)

# r = requests.get('http://iflv9.afreecatv.com/AFFLV/03/7/45/9_03_1495952609691177_2147483647_L.jpg')

r = requests.get('http://bpic.588ku.com/back_pic/04/28/17/53583d40b2444bc.jpg!/fh/300/quality/90/unsharp/true/compress/true', hooks=dict(response=response_hook))

with open('3.jpg', 'wb') as f:
    f.write(r.content)
