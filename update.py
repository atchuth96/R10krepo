import requests
import base64
import git
from git import Repo

r=Repo()
tags=r.tags
lasttag=tags[-1]
print(lasttag)
