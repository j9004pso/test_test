#ライブラリのインポート
import json
import csv

#ファイルパスの入出力
fileIn = "data.json"
fileOut = "output.csv"

#jsonファイルの読み込み
json_open = open(fileIn, 'r')
json_load = json.load(json_open)

#書込むデータの格納辞書型
outDict = {}
glNo = 0


def Recursion(x, argStr):
    global glNo
    headStr = ""
    nextStr = ""
    #文字列の時
    if type(x) is str: 
        outElement = "{0}_{1}".format(glNo, argStr)
        glNo += 1
        outDict.update({outElement: x})
    #リスト型
    if type(x) is list: 
        for lp in x:
            nextStr = "{0}{1}".format(argStr, headStr)
            Recursion(lp, nextStr)
            nextStr = ""
    #辞書型
    if type(x) is dict: 
        for lp in x.items():
            if argStr != "":
                headStr = "__"
            nextStr += "{0}{1}{2}".format(argStr, headStr, lp[0].strip())
            Recursion(x[lp[0]], nextStr)
            nextStr = ""

Recursion(json_load, "")

#CSVファイルに書き込み
with open(r'{0}'.format(fileOut), 'w', encoding='utf-8', newline="") as f:
    writer = csv.writer(f)
    for k, v in outDict.items():
        writer.writerow([k, v])
