import requests
import base64
import git
from git import Repo

r=Repo()
tags=r.tags
lasttag=tags[-1]
tag='1.1.3'
new_tag = repo.create_tag(tag, message='Automatic tag "{0}"'.format(tag)) 
repo.remotes.origin.push(new_tag)


