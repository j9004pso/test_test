import pandas as pd

# Excelファイルのパスとキーワードを入力
file_path = input("Excelファイルのパスを入力してください: ")
keyword = input("抽出するキーワードを入力してください: ")

# Excelファイルを読み込む
try:
    excel_data = pd.read_excel(file_path, sheet_name="Sheet1", header=None)
except Exception as e:
    print(f"Excelファイルを読み込む際にエラーが発生しました: {e}")
    exit()

# キーワードが含まれる行を見つける
found_rows = excel_data[excel_data.apply(lambda row: row.astype(str).str.contains(keyword).any(), axis=1)]

# 結果を表示する
print(found_rows)
