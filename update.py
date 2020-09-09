import requests
import base64
import os
import subprocess


stream = os.popen("git for-each-ref --sort=creatordate --format '%(refname)' refs/tags")
tagsstr = stream.read()
tags=tagsstr.splitlines()
lasttag=tags[-1]
print(lasttag)
lasttag=lasttag.replace('refs/tags/','')
print(lasttag)
lastdig=lasttag.split('.')[-1]
print(lastdig)
lastdig=int(lastdig)
lastdig=lastdig+1
lastdig=str(lastdig)

command="git tag 1.1."+lastdig
os.popen(command)
command1="git push origin master --tags --force"
os.popen(command1)
    
   


"""repo=Repo()
tags=repo.tags
lasttag=tags[-1]
tag='1.1.3'
new_tag = repo.create_tag(tag, message='Automatic tag "{0}"'.format(tag)) 
repo.remotes.origin.push(new_tag)"""


