#!/bin/bash
counter=0
today=$(date +%d-%m-%Y)
oneweekago=$(date +%d-%m-%Y -d 'last Sunday')
serverName="Gran_Minearia"
folderName="mods"
main='minearia.com/public_html/web'

if [[ ! -f /home/tamipramos/forge/logs/backup.log ]]; then
        echo -e "[*] Creando carpetas y primera copia completa..."
        mkdir -p /var/www/$main/$serverName/$folderName/
        echo -e "\n[!] /var/www/"$main/$serverName" creada."
        echo -e "[!] /var/www/"$main/$serverName"/"$folderName" creada.\n"
        bash bash /home/tamipramos/forge/logger.sh "Creando backup completo de mods." backup
        tar -cvf /var/www/$main/$serverName/$folderName/"MODS_LIST_`date +%d-%m-%Y`.tar" /home/tamipramos/forge/$folderName
        rar a /var/www/$main/$serverName/$folderName/"MODS_LIST_`date +%d-%m-%Y`.rar" /home/tamipramos/forge/$folderName
        echo -e "\n[*] Copia completa realizada con éxito. \n" && ls /var/www/$serverName/$folderName/*
        bash /home/tamipramos/forge/logger.sh "Copia completa realizada con éxito." backup
else
        echo -e "[*] Creando copia diferencial..."
        rm /var/www/$main/$serverName/$folderName/*.rar
        rm /var/www/$main/$serverName/$folderNAme/*.tar
        tar -cvf /var/www/$main/$serverName/$folderName/"MODS_LIST_`date +%d-%m-%Y`.tar" /home/tamipramos/forge/$folderName -N $oneweekago>
        rar a /var/www/$main/$serverName/$folderName/"MODS_LIST_`date +%d-%m-%Y`.rar" /home/tamipramos/forge/$folderName && chmod 777 *.rar
        bash /home/tamipramos/forge/logger.sh "Creando copia diferencial de mods." backup
        echo -e "[*] Copia diferencial creada.\n" && ls /var/www/$main/$serverName/$folderName/*
        bash /home/tamipramos/forge/logger.sh "Copia diferencial creada." backup
fi

sudo systemctl restart apache2