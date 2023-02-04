import os
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
                print(f'El archivo {file} tiene {counter} lineas de código de los cuales {commentcounter} son comentarios.')

                