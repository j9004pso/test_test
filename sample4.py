import json
import csv

fileIn = "data.json"
fileOut= "out_vpc.csv"

json_open = open(fileIn, 'r')
json_load = json.load(json_open)

outDict = {}
glNo = 0

def nestLoop(el,argStr):
    global glNo
    headStr = ""
    nextStr = ""
    if type(el) is str: # 文字列
        nowNo = f'{glNo:03}'
        outElement = "{0}___{1}".format(nowNo,argStr)
        glNo += 1
        outDict.update( { outElement : el } )
    if type(el) is list: # リスト型
        for lp in el:
            nextStr = "{0}{1}".format(argStr , headStr)
            nestLoop( lp , nextStr)
            nextStr = ""
    if type(el) is dict: # 辞書型
        for lp in el.items():
            if argStr != "":
                headStr = "__"
            nextStr += "{0}{1}{2}".format( argStr , headStr , lp[0].strip() )
            nestLoop( el[ lp[0] ] , nextStr)
            nextStr = ""

nestLoop(json_load,"")

with open(r'{0}'.format(fileOut),'w',encoding='utf-8',newline="") as f:
    writer = csv.writer(f)
    for k, v in outDict.items():
        writer.writerow([k, v])
