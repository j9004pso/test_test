import json
import csv

# JSONファイルを読み込む
with open('profile.json', 'r') as json_file:
    data = json.load(json_file)

# CSVファイルにデータを書き込む
with open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    
    # JSONデータが辞書の場合
    if isinstance(data, dict):
        for key, value in data.items():
            writer.writerow([key, value])  # ペアをそれぞれの行に書き込む
    
    # JSONデータがリストの場合
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                for key, value in item.items():
                    writer.writerow([key, value])  # ペアをそれぞれの行に書き込む
            else:
                writer.writerow([item])  # リスト内の要素を個別の行に書き込む
