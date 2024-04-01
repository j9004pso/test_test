import json
import csv

def flatten_json(data, prefix=''):
    """
    再帰的にJSONデータをフラット化する関数
    """
    flat_data = {}
    for key, value in data.items():
        if isinstance(value, dict):
            flat_data.update(flatten_json(value, prefix + key + '.'))
        else:
            flat_data[prefix + key] = value
    return flat_data

def json_to_csv(json_file, csv_file):
    # JSONファイルを読み込む
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # CSVファイルにデータを書き込む
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # ヘッダーを書き込む
        header_written = False
        for item in data['policies']:
            flat_policy = flatten_json(item)
            if not header_written:
                writer.writerow(flat_policy.keys())
                header_written = True
            
            # データを書き込む
            writer.writerow(flat_policy.values())

# JSONファイル名とCSVファイル名を指定して関数を呼び出す
json_file = 'data.json'  # ここにJSONファイルのパスを指定してください
csv_file = 'output.csv'  # ここに出力するCSVファイルのパスを指定してください
json_to_csv(json_file, csv_file)
