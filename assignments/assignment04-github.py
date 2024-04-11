#Write a program in python that will read a file from a repository, 
#The program should then replace all the instances of the text "Andrew" with your name. 
#The program should then commit those changes and push the file back to the repository (You will need authorisation to do this).
#I do not need to see your keys (see lab2, to follow)
#Handup: Push the program as assignment04-github.py to assignments repository.
#Marks: Marks will be given for the functionality and layout of the code; I do expect minimal comments to indicate you know what the program is doing.
#token: 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

#Source to read file: https://python-forum.io/thread-26072.html

from github import Github


g = Github("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")

repo = g.get_repo("darachg22/WSAA-coursework")

file_content = repo.get_contents("assignments/Andrew.txt")

print(file_content)



