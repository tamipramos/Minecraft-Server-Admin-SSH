import os, datetime
totalcode=0
totalcomment=0
date=datetime.datetime.now()
for root, dirs, files in os.walk("./"):
    for file in files:
        if file.endswith(".py") and dirs != "management" and dirs != "config" and dirs != '.id_rsa':
            counter=0
            commentcounter=0
            with open(os.path.join(root, file), 'r',encoding="utf8") as f:
                for line in f.readlines():
                    if line.startswith('#') or '#' in line:
                        commentcounter+=1
                    if line.startswith('\''):
                        commentcounter+=1
                    counter+=1
                totalcode+=counter
                totalcomment+=commentcounter
                print(f'- The file {file} has  `[{counter}]`  of code, which  [{commentcounter}]  are comments')
print(f'#### TOTAL LINES OF CODE: `{totalcode}`')
print(f'#### TOTAL LINES OF COMMENTS: `{totalcomment}`')
print(f'at {date.strftime("%d-%b-%Y")}')

                