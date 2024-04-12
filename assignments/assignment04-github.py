#Source to read file: https://python-forum.io/thread-26072.html

#from github import Github

#g = Github("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")
#repo = g.get_repo("darachg22/WSAA-coursework")
#content = repo.get_contents("assignments/Andrew.txt")
#repo.update_file(content.path, "more tests", "more tests", content.sha, branch="test")
from github import Github
from config import config

# Connect to GitHub using the token from config.py
github_token = config["github_token"]
g = Github(github_token)

# Get the repository
repo = g.get_repo("darachg22/WSAA-coursework")

# Get the file contents
file = repo.get_contents("assignments/Andrew.txt", ref="main")
file_path = file.path

# Modify the file content
file_content = (file.decoded_content).decode('utf-8').replace("Andrew", "Darach")
file_sha = file.sha

# Update the file
repo.update_file(file_path, "FileUpdated", file_content, file_sha, branch="main")



