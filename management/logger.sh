#!/bin/bash

statusFile=/home/tamipramos/forge/logs/status.log

backupFile=/home/tamipramos/forge/logs/backup.log

if [ -f $backupFile ];then
        if [[ "$2" == "backup" ]];then
                echo "[BACKUP][`date +'%d/%m/%Y %T'`] "$1 >> $backupFile
        fi
else
        touch $backupFile
        if [[ "$2" == "backup" ]];then
                echo "[BACKUP][`date +'%d/%m/%Y %T'`] "$1 >> $backupFile
        fi
fi
if [ -f $statusFile ]; then

        if [[ "$2" == "status" ]];then
                echo "[STATUS][`date +'%d/%m/%Y %T'`] "$1 >> $statusFile
        fi
else
        touch $statusFile
        if [[ "$2" == "status" ]];then
                echo "[STATUS][`date +'%d/%m/%Y %T'`] "$1 >> $statusFile
        fi
fi