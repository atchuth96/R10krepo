import requests
import base64
from git import Git

g = Git for-each-ref --sort=creatordate --format '%(refname)' refs/tags
print(g)
