import os
import File_Delete

#指定されたフォルダ内およびそのサブフォルダ内の特定の拡張子のファイルを削除する
def delete_extension(folder_path, extension):

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(extension):
                file_path = os.path.join(root, file_name)
                os.remove(file_path)
                
print("検索方法：File_Delete.delete_extension(r'',r'.txt')")

"""呼び出し方
import File_Delete
File_Delete.delete_extension(r'',r'.txt')

"""
