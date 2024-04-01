import requests

#JenkinsにジョブにアクセスするためのURL
jenkins_job_url = "http://localhost:8080/job/File_Delete/build"

#ユーザ名とパスワードを設定し、Jenkinsにアクセスする
try:
    response = requests.post(jenkins_job_url, auth=("j9004pso", "11b1f0f92e4249326b36a8d5e26084452c"))

    response.raise_for_status()

#201は成功。それ以外のコードはエラー。
    if response.status_code == 201:
        print("正常")
    else:
        print("エラーが発生")

#エラーが起きたときにどんなエラーだったかをエラーコードとともに表示。
except requests.exceptions.RequestException as e:
    print("リクエスト中にエラーが発生しました:", e)
except Exception as e:
    print("予期しないエラーが発生しました:", e)
