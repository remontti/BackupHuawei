#!/bin/sh
#
DIR='/root/scripts/BackupHuawei'
DIRSAVE='/home/backups/huawei'
cd ${DIR}
DATABKP=`date +%Y-%m-%d`
for var in `cat ${DIR}/DISPOSITIVOS`;do        
      IP=`echo $var | cut -d , -f 1`
      USER=`echo $var | cut -d , -f 2`
      PASS=`echo $var | cut -d , -f 3`
      PORTA=`echo $var | cut -d , -f 4`
      NAME=`echo $var | cut -d , -f 5`
      TIPO=`echo $var | cut -d , -f 6`

      DIRBKP="${DIRSAVE}/${NAME}/"
      if [ ! -d "$DIRBKP" ]; then
        mkdir ${DIRSAVE}/${NAME}/
      fi
      /root/scripts/BackupHuawei/backup-huawei.py ${IP} ${USER} ${PASS} ${PORTA} ${DATABKP}_${NAME} ${TIPO}
      mv *.txt ${DIRSAVE}/${NAME}/
      sleep 1
done