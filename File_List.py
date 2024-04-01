import os

#指定されたフォルダ内およびそのサブフォルダ内のファイルを一覧で表示する
def file_in_folder(folder_path):

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, folder_path)
            print(relative_path)

print("検索方法：File_List.file_in_folder(r'')")

"""呼び出し方
import File_List
File_List.file_in_folder(r'')
"""

