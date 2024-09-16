from token_and_name import access_token, name_repo
import requests
from github import Github

login = Github(access_token)
user = login.get_user()
username = input('Введите ваше уникальное имя на github: ')

def del_repo(username, name_repo, access_token):
    url = f"https://api.github.com/repos/{username}/{name_repo}"
    headers = {"Authorization": f"token {access_token}"}
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print("репозиторий удален")
    elif response.status_code == 404:
        print("репозиторий не найден")
    else:
        print("ошибка выполнения")
        
del_repo(username, name_repo, access_token)
