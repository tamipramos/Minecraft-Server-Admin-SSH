#!/bin/bash
counter=0
today=$(date +%d-%m-%Y)
oneweekago=$(date +%d-%m-%Y -d 'last Sunday')
serverName="Gran_Minearia"
folderName="mods"

for file in $(ls /var/www/html/$serverName/$folderName/*.rar); do
        if [ -f $file ]; then
                echo $counter
                counter=$counter+1
        else
                continue
        fi
        if [[ $counter -gt 5 ]];then
                rm /var/www/html/$serverName/$folderName/*.rar
                rm /var/www/html/$serverName/$folderName/*.tar
                bash /home/tamipramos/forge/logger.sh "Purga de archivos >5#" backup
        fi

done

if [[ ! -f /var/www/reference ]]; then
        echo -e "[*] Creando carpetas y primera copia completa..."
        mkdir -p /var/www/html/$serverName/$folderName/
        echo -e "\n[!] /var/www/html/"$serverName" creada."
        echo -e "[!] /var/www/html/"$serverName"/"$folderName" creada.\n"
        bash bash /home/tamipramos/forge/logger.sh "Creando backup completo de mods." backup
        tar -cvf /var/www/html/$serverName/$folderName/"MODS_LIST_`date +%d-%m-%Y`.tar" $folderName
        rar a /var/www/html/$serverName/$folderName/"MODS_LIST_`date +%d-%m-%Y`.rar" $folderName
        echo -e "\n[*] Copia completa realizada con éxito. \n" && ls /var/www/html/$serverName/$folderName/*
        bash /home/tamipramos/forge/logger.sh "Copia completa realizada con éxito." backup
else
        echo -e "[*] Creando copia diferencial..."
        tar -cvf /var/www/html/$serverName/$folderName/"MODS_LIST_`date +%d-%m-%Y`.tar" $folderName -N $oneweekago
        rar a /var/www/html/$serverName/$folderName/"MODS_LIST_`date +%d-%m-%Y`.rar" $folderName
        bash /home/tamipramos/forge/logger.sh "Creando copia diferencial de mods." backup
        echo -e "[*] Copia diferencial creada.\n" && ls /var/www/html/$serverName/$folderName/*
        bash /home/tamipramos/forge/logger.sh "Copia diferencial creada." backup
fi