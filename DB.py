import pymongo
import time
client = pymongo.MongoClient('localhost', 27017)
Enterprise_Genius = client["Enterprise_Genius"]
def insert_announcement_info(info):
    announcement = Enterprise_Genius["announcement"]
    announcement_info = {"date":time.strftime("%Y-%m-%d", time.localtime()),"announcement":info}
    announcement.insert_one(announcement_info)
def search_announcement_info(date=time.strftime("%Y-%m-%d", time.localtime())):
    announcement = Enterprise_Genius["announcement"]
    infos = announcement.find({"date":date})
    data = ""
    for info in infos:
        data = data+ info["announcement"] +"\n"
    return data
def insert_purchase_order(name,goods,number):
    purchase_order =  Enterprise_Genius["purchase_order"]
    purchase_order_info = {"name":name,"goods":goods,"number":number,"flag":False}
    purchase_order.insert_one(purchase_order_info)
def search_purchase_order(name):
    purchase_order = Enterprise_Genius["purchase_order"]
    infos = purchase_order.find({"name": name})
    data = ""
    for info in infos:
        if info["flag"] == False:
            data = data+"货物："+ info["goods"] +"  数量："+info["number"]+"\n"
    return data
def update_purchase_order(name,goods):
    purchase_order = Enterprise_Genius["purchase_order"]
    purchase_order.update({"name": name, "goods": goods}, {"$set": {"flag": True}})
    return search_purchase_order(name)


# print(search_announcement_info("2017-09-03"))
# insert_announcement_info("nihaoa ")
# insert_purchase_order("陈瑞锋","盐","2t")
# print(search_purchase_order("陈瑞锋"))