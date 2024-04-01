from git import Repo

# クローン元のリポジトリのURL
repository_url = 'https://github.com/j9004pso/push_test.git'

# クローン先のディレクトリパス
clone_to_directory = 'C:/Users/b23a0005/clone'

try:
    # リポジトリをクローンする
    Repo.clone_from(repository_url, clone_to_directory)
    print("リポジトリをクローンしました。")
except Exception as e:
    print("リポジトリのクローン中にエラーが発生しました:", e)

