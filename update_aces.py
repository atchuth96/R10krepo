import os
import sys

appname=sys.argv[1]
buildNum=sys.argv[2]
matched=False
updated=False
print("Updating "+appname+" for build "+buildNum)
contentline=open("puppetfile.txt","r")
content=contentline.readlines()
print(content)
for i in range(0,len(content)):
    if (i+2) < len(content):        
        if appname in content[i]:
            matched=True
            if matched and not updated:
                k=i+2
                newcontent=":ref => '1.1."+buildNum+"'"
                print("Replacing "+content[k]+" with "+newcontent)
                content[k]=newcontent
                updated=True
print(content)
f = open("puppetfile.txt", "w")
new_file_contents = "\n".join(content)
f.write(new_file_contents)
f.close()
                


