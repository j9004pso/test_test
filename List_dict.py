#リスト
my_list = [1,2,3,4,5]

my_list.append(6) #appendで要素追加 [1, 2, 3, 4, 5, 6]
My_list.insert(2,10) #insert(インデックス番号,値)は値の追加 [1, 2, 10, 3, 4, 5, 6]
my_list.append(5) #appendで要素追加 [1, 2, 10, 3, 4, 5, 6, 5]

del my_list[1] #delで要素の削除 [1, 10, 3, 4, 5, 6, 5]
my_list.remove(1) #指定した値を削除。ただし同じ値が複数あっても削除されるのは先にある値だけ。[1, 10, 3, 4, 6, 5]
my_list.pop() #末尾の値を取り出し削除 5 [1, 10, 3, 4, 6]
my_list.pop(2) #指定したインデックスの値を取り出し削除 3 [1, 10, 4, 6]

my_list[2] = 15 #リストの要素の値を更新 [1, 10, 15, 6]
len(my_list) #リストの長さ 4

my_list.sort() #昇順にソート [1, 6, 10, 15]
my_list.sort(reverse=True) #降順にソート [15, 10, 6, 1]



#辞書
mydict = {"apple":1, "orange":2, "banana":3}

val = mydict["apple"] #要素へのアクセス

print("orange" in mydict.keys()) #keysが含まれているか
print(5 in mydict.values()) #valuesが含まれているか

mydict["peach"] = 4 #新しくkeys,valuesを追加
mydict.setdefault("peach", 4) #setdefaultメソッドでも可

#辞書型の要素に辞書を追加
mydict1 = {"apple":1, "orange":2, "banana":3}
mydict2 = {"peach":4, "cherry":5, "melon":6}
mydict1["dict"] = mydict2
print(mydict1)

#要素の削除
mydict = {"apple":1, "orange":2, "banana":3}
mydict.pop("orange")
print(mydict)

#全ての要素の削除
mydict = {"apple":1, "orange":2, "banana":3}
mydict.clear()
print(mydict)