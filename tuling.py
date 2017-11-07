import requests
import json

key = "xxxxxxxxxxx"
data = {"key":key,"info":"xx","userid":"123"}

wb_data = requests.post("http://www.tuling123.com/openapi/api",data=data)
text = json.loads(wb_data.text)
print(text["text"])