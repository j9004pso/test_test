import json
import csv

# JSONファイルを読み込む
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# CSVファイルにデータを書き込む
with open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    
    # JSONデータが辞書の場合
    if isinstance(data, dict):
        writer.writerow(data.keys())  # ヘッダー行を書き込む
        writer.writerow(data.values())  # データ行を書き込む
    
    # JSONデータがリストの場合
    elif isinstance(data, list):
        if data:
            # ヘッダー行を書き込む
            writer.writerow(data[0].keys() if isinstance(data[0], dict) else range(len(data[0])))
            
            # データ行を書き込む
            for item in data:
                writer.writerow(item.values() if isinstance(item, dict) else item)