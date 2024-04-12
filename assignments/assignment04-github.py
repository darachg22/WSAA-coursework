#Source to read file: https://python-forum.io/thread-26072.html

#from github import Github

#g = Github("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")
#repo = g.get_repo("darachg22/WSAA-coursework")
#content = repo.get_contents("assignments/Andrew.txt")
#repo.update_file(content.path, "more tests", "more tests", content.sha, branch="test")

from github import Github

#Connect to GitHub
g = Github("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")
repo = g.get_repo("darachg22/WSAA-coursework")

#source code used: https://github.com/santiagomoneta/pygithub-example/blob/main/main.py
#The first line here gets the text from the path given, using the branch as reference.
file = repo.get_contents("assignments/Andrew.txt", ref="main")
#This line create the file path to use again. 
file_path = file.path
#The following line reads the file then converts it before replacing the words 'Andrew' with 'Darach'.
file_content = (file.decoded_content).decode('utf-8').replace("Andrew", "Darach") 
#This line retrieves something called the Secure Hash Algorithim, that identifies the content of the text file and verifies the changes. 
file_sha = file.sha
#Here the text file gets updated with the new changes. 
repo.update_file(file_path, "FileUpdated", file_content, file_sha, branch="main")



