import itchat
import requests
from bs4 import BeautifulSoup
import json
import translation
import taobaosp
import DB
import natural_language_processing


@itchat.msg_register(itchat.content.TEXT)
def echo(msg):
    instruction = msg.text.split(" ")[0]
    if instruction == "翻译":
        back = translation.trans(msg.text.split(" ",1)[-1])
    elif instruction == "价格":
        back = taobaosp.get_info(msg.text.split(" ")[-1])
    elif instruction == "公告":
        if(msg.text.split(" ")[-1]!="公告"):
            back = DB.search_announcement_info(msg.text.split(" ")[-1])
        else:
            back = DB.search_announcement_info()
    elif instruction == "发布公告":
        DB.insert_announcement_info(msg.text.split(" ",1)[-1])
        back = "已经成功发布"
    else:
        try:
            NLPlist = natural_language_processing.NLP(msg.text)
            if NLPlist[1] == "采购单":
                back = DB.search_purchase_order(NLPlist[0])
            elif NLPlist[1] == "新增采购":
                 DB.insert_purchase_order(NLPlist[0], NLPlist[2], NLPlist[3])
                 back = "采购添加已经成功"
            elif NLPlist[1] == "采购提交":
                 back = DB.update_purchase_order(NLPlist[0],NLPlist[2])
            else:
                 back = tulingback(msg.text)
        except:
            back = tulingback(msg,text)
    print("in:"+msg.text)
    print("out:"+back)
    return back
def getres(intext):
    key = "eGI1Q0VRejg9SC9ZT2xiPW9IU1JVNStqeGhJQUFBPT0"
    url = "http://api.douqq.com/?key="+key+"&msg="+intext
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,"lxml")
    return soup.select("body")[0].text
def tulingback(intext):
    key = "971309069ab84ae1b7fa8dba5836658c"
    data = {"key": key, "info":intext, "userid": "123"}
    wb_data = requests.post("http://www.tuling123.com/openapi/api", data=data)
    text = json.loads(wb_data.text)
    return text["text"]
if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()
