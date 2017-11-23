import json
import requests
import random
import hashlib

#从百度申请
appid = '----------'
secretKey = '------------'

def trans(conent):
    url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
    salt = random.randint(32768,65536)
    sign = appid + conent +str(salt)+secretKey
    sign = sign.encode("UTF-8")
    m = hashlib.md5()
    m.update(sign)
    md5value = m.hexdigest()
    myurl = url +'?appid='+appid+'&q='+conent+'&from='+"auto"+'&to='+"zh"+'&salt='+str(salt)+'&sign='+md5value
    data = requests.get(myurl)
    target2 = json.loads(data.text)
    src = target2["trans_result"][0]["dst"]
    return src
if __name__ == '__main__':
    trans("hello world")
