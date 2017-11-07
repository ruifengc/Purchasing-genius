import requests
import re
def getHTML(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def getGOOD(html):
    glist=[]
    rgood = re.compile(r'"raw_title":"(.+?)"').findall(html)
    rpri = re.compile(r'"view_price":"([\d\.]+)"').findall(html)
    rlocal = re.compile(r'"item_loc":(.+?)"').findall(html)
    for i in range(len(rgood)):
        glist.append([rgood[i],rpri[i],rlocal[i]])
    return glist
def showGOOD(goodlist):
    tplt = '{:4}\t{:8}\t{:16}'
    datalist = []
    datalist.append(tplt.format("序号",'价格','商品名称'))
    for i in range(len(goodlist)):
        good = goodlist[i]
        datalist.append(tplt.format(i+1,good[1],good[0]))
    return datalist

def get_info(goodname):
    rooturl = 'https://s.taobao.com/search?q='
    deep= 1
    goodlist = []
    for i in range(deep):
        url = rooturl+goodname+'&s='+str(i*44)
        html = getHTML(url)
        # print(url)
        goodlist += getGOOD(html)
    goodlist = showGOOD(goodlist)
    strgood  = ""
    for i in goodlist[:10]:
        strgood += i+"\n"
    return strgood
if __name__ == '__main__':
    print(get_info("铅笔"))
