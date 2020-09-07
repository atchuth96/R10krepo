import requests
import base64
import git
from git import Repo

r=Repo()
print(r.tags)
print(type(r.tags))
