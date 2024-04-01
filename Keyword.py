import os
import Keyword

#ファイル内で指定された文字列を検索し、その行を表示する
def keyword_search(file_path, target_string):

    with open(file_path, "r", encoding="utf-8") as file_data:
        for line in file_data:
            if target_string in line:
                print(line)
                
print("検索方法：Keyword.keyword_search(r'','hello')")

# ファイルを指定して検索を実行
#Keyword.keyword_search(r"C:\Users\b23a0005\OneDrive - TCS-G\デスクトップ\akiyama\test2.txt", "Akiyama")
