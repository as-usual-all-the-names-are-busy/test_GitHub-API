from token_and_name import access_token, name_repo
import requests
from github import Github

login = Github(access_token)
user = login.get_user()

def yes_or_no(name_repo):
    my_repos = user.get_repos()
    my_repos = list(map(lambda i: i.name, my_repos))
    if name_repo in my_repos:
        print("такой репозиторий уже существует")
    else:
        print("такого репозитория нет, можно создавать")
yes_or_no(name_repo)
