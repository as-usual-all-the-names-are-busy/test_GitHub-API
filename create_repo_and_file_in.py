from token_and_name import access_token, name_repo
import requests
from github import Github

login = Github(access_token)
user = login.get_user()

def create_repo(name_repo):
    new_repo = user.create_repo(name_repo)
    new_repo.create_file("New-File.txt", "new commit", "Data Inside the File")

create_repo(name_repo)
